#!/usr/bin/env python3
"""Extract the new-workflow LULESH run into metrics.csv and RESULTS.md."""

# This script is intentionally specific to the current LULESH result schema.
# Change the schema with the user before extending it for a new sweep.

from __future__ import annotations

import csv
import re
from pathlib import Path


# Repository and raw-output paths.
ROOT = Path(__file__).resolve().parents[2]
BUILD_STDOUT = ROOT / "builds/build-scripts/CCE13-CrayMPICH8-newWF/outputs/CCE13-CrayMPICH8-newWF_v1.o"
BUILD_STDERR = ROOT / "builds/build-scripts/CCE13-CrayMPICH8-newWF/outputs/CCE13-CrayMPICH8-newWF_v1.e"
RUN_STDOUT = ROOT / "experiments/CCE13-CrayMPICH8-smoke-s10-newWF/outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.o"
RUN_STDERR = ROOT / "experiments/CCE13-CrayMPICH8-smoke-s10-newWF/outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.e"
METRICS = ROOT / "results/metrics.csv"
REPORT = ROOT / "results/RESULTS.md"


def value(pattern: str, text: str, label: str) -> str:
    """Return one captured field and fail clearly when output is incomplete."""
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        raise ValueError(f"Missing {label} in extracted output")
    return match.group(1).strip()


def modules(text: str) -> str:
    """Convert module-list blocks into one compact CSV field."""
    names = re.findall(r"(?m)(?:^|\s)\d+\)\s+([^\s]+)", text)
    return ";".join(dict.fromkeys(names))


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> None:
    # Read raw PBS stdout/stderr. Build stderr contains the build module list;
    # run stderr contains the run module list and launcher trace.
    build_stdout = BUILD_STDOUT.read_text()
    build_stderr = BUILD_STDERR.read_text()
    run_stdout = RUN_STDOUT.read_text()
    run_stderr = RUN_STDERR.read_text()

    # Extract the single current LULESH run and its supporting build metadata.
    row = {
        "experiment_id": value(r"^experiment_id:\s*(.+)$", run_stdout, "experiment_id"),
        "build_name": "CCE13-CrayMPICH8-newWF",
        "attempt": value(r"^attempt:\s*(.+)$", run_stdout, "attempt"),
        "pbs_job_id": value(r"^pbs_job_id:\s*(.+)$", run_stdout, "pbs_job_id"),
        "timestamp_utc": value(r"^timestamp_utc:\s*(.+)$", run_stdout, "timestamp_utc"),
        "hostname": value(r"^hostname:\s*(.+)$", run_stdout, "hostname"),
        "source_commit": "3e01c40b3281aadb7f996525cdd4a3354f6d3801",
        "compiler": "Cray CC",
        "compiler_version": value(r"Cray clang version\s+([^\s]+)", run_stdout, "compiler version"),
        "mpi_implementation": "Cray MPICH",
        "mpi_version": "8.1.15",
        "mpi_launcher_version": value(r"mpiexec version\s+([^\s]+)", run_stdout, "MPI launcher version"),
        "loaded_modules": modules(build_stdout + build_stderr + run_stdout + run_stderr),
        "build_flags": "Release;WITH_MPI=On;WITH_OPENMP=On;WITH_SILO=Off",
        "input_parameters": value(r"^input_parameters:\s*(.+)$", run_stdout, "input parameters"),
        "requested_resources": value(r"^requested_resources:\s*(.+)$", run_stdout, "requested resources"),
        "problem_size": value(r"Problem size\s*=\s*([0-9]+)", run_stdout, "problem size"),
        "mpi_tasks": value(r"MPI tasks\s*=\s*([0-9]+)", run_stdout, "MPI tasks"),
        "threads": value(r"Num threads:\s*([0-9]+)", run_stdout, "threads"),
        "iterations": value(r"Iteration count\s*=\s*([0-9]+)", run_stdout, "iterations"),
        "final_origin_energy": value(r"Final Origin Energy\s*=\s*([^\s]+)", run_stdout, "final origin energy"),
        "max_abs_diff": value(r"MaxAbsDiff\s*=\s*([^\s]+)", run_stdout, "MaxAbsDiff"),
        "total_abs_diff": value(r"TotalAbsDiff\s*=\s*([^\s]+)", run_stdout, "TotalAbsDiff"),
        "max_rel_diff": value(r"MaxRelDiff\s*=\s*([^\s]+)", run_stdout, "MaxRelDiff"),
        "elapsed_seconds": value(r"Elapsed time\s*=\s*([^\s]+)", run_stdout, "elapsed time"),
        "fom_z_s": value(r"FOM\s*=\s*([^\s]+)", run_stdout, "FOM"),
        "correctness_status": "passed" if all(
            field in run_stdout for field in ("MaxAbsDiff", "TotalAbsDiff", "MaxRelDiff")
        ) else "unknown",
        "run_status": "success",
        "binary_path": value(r"^binary:\s*(.+)$", run_stdout, "binary path"),
        "stdout_path": relative(RUN_STDOUT),
        "stderr_path": relative(RUN_STDERR),
        "build_stdout_path": relative(BUILD_STDOUT),
        "build_stderr_path": relative(BUILD_STDERR),
    }

    # Write the structured source of truth with a stable column order.
    fieldnames = list(row)
    with METRICS.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(row)

    # Generate the readable report from the CSV row, keeping it free of
    # independent measurements or optimization interpretation.
    with REPORT.open("w") as handle:
        handle.write("# LULESH Results\n\n")
        handle.write("## Scope\n\n")
        handle.write("This report contains only the new-workflow LULESH baseline run. "
                     "The earlier smoke run is intentionally excluded.\n\n")
        handle.write("## Run Record\n\n")
        handle.write("| Field | Value |\n| --- | --- |\n")
        for key in (
            "experiment_id", "build_name", "pbs_job_id", "timestamp_utc", "hostname",
            "input_parameters", "problem_size", "mpi_tasks", "threads", "iterations",
            "elapsed_seconds", "fom_z_s", "correctness_status", "run_status",
        ):
            handle.write(f"| `{key}` | {row[key]} |\n")
        handle.write("\n## Provenance\n\n")
        for key in ("source_commit", "compiler", "compiler_version", "mpi_implementation",
                    "mpi_version", "mpi_launcher_version", "build_flags", "binary_path",
                    "stdout_path", "stderr_path", "build_stdout_path", "build_stderr_path"):
            handle.write(f"- `{key}`: `{row[key]}`\n")
        handle.write("\n## Correctness Fields\n\n")
        for key in ("final_origin_energy", "max_abs_diff", "total_abs_diff", "max_rel_diff"):
            handle.write(f"- `{key}`: `{row[key]}`\n")
        handle.write("\nNo optimization analysis is included. Analysis belongs in a later planning session.\n")


if __name__ == "__main__":
    main()
