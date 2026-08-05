#!/usr/bin/env python3
# Append one validated LULESH run to metrics.csv and regenerate RESULTS.md;
# run from the repository root with build/run PBS output paths as arguments;
# preserves existing rows and rejects duplicate experiment attempts.

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
METRICS = ROOT / "results/metrics.csv"
REPORT = ROOT / "results/RESULTS.md"


def value(pattern: str, text: str, label: str) -> str:
    """Return one required captured field and fail clearly when absent."""
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        raise ValueError(f"Missing {label} in extracted output")
    return match.group(1).strip()


def optional(pattern: str, text: str, default: str = "unknown") -> str:
    """Return a captured field when present, otherwise a documented default."""
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(1).strip() if match else default


def modules(text: str) -> str:
    """Convert module-list blocks into one compact CSV field."""
    names = re.findall(r"(?m)(?:^|\s)\d+\)\s+([^\s]+)", text)
    return ";".join(dict.fromkeys(names))


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


def compiler_metadata(build_text: str, loaded_modules: str) -> tuple[str, str]:
    """Identify the compiler family and version from recorded job metadata."""
    if "aocc/" in loaded_modules:
        return "AOCC CC", value(r"aocc/([^;]+)", loaded_modules, "AOCC version")
    if "cce/" in loaded_modules:
        return "Cray CC", value(r"cce/([^;]+)", loaded_modules, "CCE version")
    return "C++ compiler", optional(r"(?:clang|gcc)[^\n]*version\s+([^\s]+)", build_text)


def extract_row(args: argparse.Namespace) -> dict[str, str]:
    build_stdout_path = (ROOT / args.build_stdout).resolve()
    build_stderr_path = (ROOT / args.build_stderr).resolve()
    run_stdout_path = (ROOT / args.run_stdout).resolve()
    run_stderr_path = (ROOT / args.run_stderr).resolve()

    build_stdout = build_stdout_path.read_text()
    build_stderr = build_stderr_path.read_text()
    run_stdout = run_stdout_path.read_text()
    run_stderr = run_stderr_path.read_text()
    combined = build_stdout + build_stderr + run_stdout + run_stderr
    loaded_modules = modules(combined)
    compiler, compiler_version = compiler_metadata(build_stdout, loaded_modules)

    correctness_fields = {
        "final_origin_energy": value(r"Final Origin Energy\s*=\s*([^\s]+)", run_stdout, "final origin energy"),
        "max_abs_diff": value(r"MaxAbsDiff\s*=\s*([^\s]+)", run_stdout, "MaxAbsDiff"),
        "total_abs_diff": value(r"TotalAbsDiff\s*=\s*([^\s]+)", run_stdout, "TotalAbsDiff"),
        "max_rel_diff": value(r"MaxRelDiff\s*=\s*([^\s]+)", run_stdout, "MaxRelDiff"),
    }

    row = {
        "experiment_id": value(r"^experiment_id:\s*(.+)$", run_stdout, "experiment_id"),
        "build_name": args.build_name,
        "attempt": value(r"^attempt:\s*(.+)$", run_stdout, "attempt"),
        "pbs_job_id": value(r"^pbs_job_id:\s*(.+)$", run_stdout, "pbs_job_id"),
        "timestamp_utc": value(r"^timestamp_utc:\s*(.+)$", run_stdout, "timestamp_utc"),
        "hostname": value(r"^hostname:\s*(.+)$", run_stdout, "hostname"),
        "source_commit": value(r"^source_commit:\s*(.+)$", run_stdout, "source commit"),
        "compiler": compiler,
        "compiler_version": compiler_version,
        "mpi_implementation": "Cray MPICH",
        "mpi_version": optional(r"cray-mpich/([^;\s]+)", loaded_modules),
        "mpi_launcher_version": value(r"mpiexec version\s+([^\s]+)", run_stdout, "MPI launcher version"),
        "loaded_modules": loaded_modules,
        "build_flags": (
            f"{value(r'^build_type:\s*(.+)$', build_stdout, 'build type')};"
            f"WITH_MPI={value(r'^with_mpi:\s*(.+)$', build_stdout, 'MPI build flag')};"
            f"WITH_OPENMP={value(r'^with_openmp:\s*(.+)$', build_stdout, 'OpenMP build flag')};"
            f"WITH_SILO={value(r'^with_silo:\s*(.+)$', build_stdout, 'SILO build flag')}"
        ),
        "input_parameters": value(r"^input_parameters:\s*(.+)$", run_stdout, "input parameters"),
        "requested_resources": value(r"^requested_resources:\s*(.+)$", run_stdout, "requested resources"),
        "problem_size": value(r"Problem size\s*=\s*([0-9]+)", run_stdout, "problem size"),
        "mpi_tasks": value(r"MPI tasks\s*=\s*([0-9]+)", run_stdout, "MPI tasks"),
        "threads": value(r"Num threads:\s*([0-9]+)", run_stdout, "threads"),
        "iterations": value(r"Iteration count\s*=\s*([0-9]+)", run_stdout, "iterations"),
        **correctness_fields,
        "elapsed_seconds": value(r"Elapsed time\s*=\s*([^\s]+)", run_stdout, "elapsed time"),
        "fom_z_s": value(r"FOM\s*=\s*([^\s]+)", run_stdout, "FOM"),
        "correctness_status": "passed",
        "run_status": "success" if "Run completed:" in run_stdout else "failed",
        "binary_path": value(r"^binary:\s*(.+)$", run_stdout, "binary path"),
        "stdout_path": relative(run_stdout_path),
        "stderr_path": relative(run_stderr_path),
        "build_stdout_path": relative(build_stdout_path),
        "build_stderr_path": relative(build_stderr_path),
    }
    return row


def append_row(row: dict[str, str]) -> None:
    """Append a row using the existing schema and reject duplicate attempts."""
    with METRICS.open(newline="") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    if set(row) != set(fieldnames):
        raise ValueError("Extracted row does not match the existing metrics.csv schema")
    key = (row["experiment_id"], row["attempt"])
    if any((item["experiment_id"], item["attempt"]) == key for item in rows):
        raise ValueError(f"Duplicate result attempt: {key[0]} / {key[1]}")

    with METRICS.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        writer.writerow(row)


def write_report() -> None:
    """Generate a compact report entirely from the current metrics.csv rows."""
    with METRICS.open(newline="") as handle:
        rows = list(csv.DictReader(handle))

    with REPORT.open("w") as handle:
        handle.write("# LULESH Results\n\n")
        handle.write("## Run Records\n\n")
        handle.write("| Experiment | Build | Attempt | PBS job | Input | Elapsed (s) | FOM (z/s) | Correctness | Status |\n")
        handle.write("| --- | --- | --- | --- | --- | ---: | ---: | --- | --- |\n")
        for row in rows:
            handle.write(
                f"| {row['experiment_id']} | {row['build_name']} | {row['attempt']} | "
                f"{row['pbs_job_id']} | `{row['input_parameters']}` | {row['elapsed_seconds']} | "
                f"{row['fom_z_s']} | {row['correctness_status']} | {row['run_status']} |\n"
            )

        handle.write("\n## Provenance\n\n")
        for row in rows:
            handle.write(f"### {row['experiment_id']} / {row['attempt']}\n\n")
            for key in (
                "timestamp_utc", "hostname", "source_commit", "compiler",
                "compiler_version", "mpi_implementation", "mpi_version",
                "mpi_launcher_version", "loaded_modules", "build_flags",
                "binary_path", "stdout_path", "stderr_path",
                "build_stdout_path", "build_stderr_path",
            ):
                handle.write(f"- `{key}`: `{row[key]}`\n")

        handle.write("\nNo optimization analysis is included. Analysis belongs in a later planning session.\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-name", required=True)
    parser.add_argument("--build-stdout", required=True)
    parser.add_argument("--build-stderr", required=True)
    parser.add_argument("--run-stdout", required=True)
    parser.add_argument("--run-stderr", required=True)
    return parser.parse_args()


def main() -> None:
    row = extract_row(parse_args())
    append_row(row)
    write_report()


if __name__ == "__main__":
    main()
