# LULESH Results

## Scope

This report contains only the new-workflow LULESH baseline run. The earlier smoke run is intentionally excluded.

## Run Record

| Field | Value |
| --- | --- |
| `experiment_id` | CCE13-CrayMPICH8-smoke-s10-newWF |
| `build_name` | CCE13-CrayMPICH8-newWF |
| `pbs_job_id` | 15086010.pbs101 |
| `timestamp_utc` | 2026-08-04T09:33:38Z |
| `hostname` | x1002c4s7b0n0 |
| `input_parameters` | -s 10 |
| `problem_size` | 10 |
| `mpi_tasks` | 1 |
| `threads` | 1 |
| `iterations` | 231 |
| `elapsed_seconds` | 0.35 |
| `fom_z_s` | 656.99887 |
| `correctness_status` | passed |
| `run_status` | success |

## Provenance

- `source_commit`: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- `compiler`: `Cray CC`
- `compiler_version`: `13.0.2`
- `mpi_implementation`: `Cray MPICH`
- `mpi_version`: `8.1.15`
- `mpi_launcher_version`: `1.1.6`
- `build_flags`: `Release;WITH_MPI=On;WITH_OPENMP=On;WITH_SILO=Off`
- `binary_path`: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0`
- `stdout_path`: `experiments/CCE13-CrayMPICH8-smoke-s10-newWF/outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.o`
- `stderr_path`: `experiments/CCE13-CrayMPICH8-smoke-s10-newWF/outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.e`
- `build_stdout_path`: `builds/build-scripts/CCE13-CrayMPICH8-newWF/outputs/CCE13-CrayMPICH8-newWF_v1.o`
- `build_stderr_path`: `builds/build-scripts/CCE13-CrayMPICH8-newWF/outputs/CCE13-CrayMPICH8-newWF_v1.e`

## Correctness Fields

- `final_origin_energy`: `2.720531e+04`
- `max_abs_diff`: `2.273737e-12`
- `total_abs_diff`: `1.659646e-11`
- `max_rel_diff`: `4.649603e-14`

No optimization analysis is included. Analysis belongs in a later planning session.
