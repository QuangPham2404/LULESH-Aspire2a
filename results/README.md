# `results/`

This directory contains structured result files extracted from raw output in
`experiments/`. Keep extracted results separate from raw `.o` and `.e` files.
Planning and interpretation belong in `planning/` and are handled in a later
analysis session.

## Layout

```text
results/
├── README.md
├── metrics.csv
├── RESULTS.md
└── scripts/
```

- `metrics.csv`: structured source of truth for extracted run data.
- `RESULTS.md`: human-readable report generated from `metrics.csv`.
- `scripts/`: extraction, parsing, or transformation scripts.

## CSV schema

For LULESH, one row represents one completed application run. A repeated run
is another row with its own attempt, PBS job, node, and measurements. Build
metadata is recorded in the same row because each run refers to one successful
build.

The current columns are:

| Column | Meaning | Units or format |
| --- | --- | --- |
| `experiment_id` | Application experiment identifier | text |
| `build_name` | Build used by the run | text |
| `attempt` | Run attempt identifier | text |
| `pbs_job_id` | PBS run job identifier | text |
| `timestamp_utc` | Run start timestamp | UTC ISO-8601 |
| `hostname` | Allocated execution node | text |
| `source_commit` | LULESH source revision | Git commit |
| `compiler` | Compiler used for the build | text |
| `compiler_version` | Compiler version | text |
| `mpi_implementation` | MPI implementation | text |
| `mpi_version` | MPI implementation version | text |
| `mpi_launcher_version` | Launcher/PALS version | text |
| `loaded_modules` | Modules loaded for the run | semicolon-separated text |
| `build_flags` | Build type and feature flags | semicolon-separated text |
| `input_parameters` | LULESH input arguments | text |
| `requested_resources` | PBS resource request | text |
| `problem_size` | LULESH problem-size argument | integer |
| `mpi_tasks` | MPI task count | integer |
| `threads` | Thread count | integer |
| `iterations` | Completed iterations | integer |
| `final_origin_energy` | Final origin energy | LULESH units |
| `max_abs_diff` | Maximum absolute energy difference | LULESH units |
| `total_abs_diff` | Total absolute energy difference | LULESH units |
| `max_rel_diff` | Maximum relative energy difference | dimensionless |
| `elapsed_seconds` | LULESH elapsed time | seconds |
| `fom_z_s` | LULESH figure of merit | zones/second |
| `correctness_status` | Observed correctness result | `passed`, `failed`, or `unknown` |
| `run_status` | Run completion status | `success` or `failed` |
| `binary_path` | Successful build binary | path |
| `stdout_path` | Raw run stdout path | repository-relative path |
| `stderr_path` | Raw run stderr path | repository-relative path |
| `build_stdout_path` | Raw build stdout path | repository-relative path |
| `build_stderr_path` | Raw build stderr path | repository-relative path |

The schema is application- and experiment-specific. Before each new
optimization sweep, decide required columns with the user and document the
decision here. New completed runs normally add rows. Add or change columns
only after discussing and recording the schema change with the user.

Do not rely on PBS exit status alone. Confirm that expected LULESH output is
present and record the observed correctness status.
