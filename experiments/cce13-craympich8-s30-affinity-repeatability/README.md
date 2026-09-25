# cce13-craympich8-s30-affinity-repeatability

Controlled affinity and repeatability validation for TASK-001: repeat the
existing CCE13 Release LULESH binary at 1 MPI rank with 1 and with 8 OpenMP
threads, three repetitions each, under one controlled 8-CPU PBS allocation
with explicit thread-affinity settings. This is a validation experiment, not
an optimization sweep; the binary is not rebuilt.

- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0`
- build provenance: `builds/build-scripts/CCE13-CrayMPICH8-newWF/` (Release,
  `WITH_MPI=On`, `WITH_OPENMP=On`, `WITH_SILO=Off`; effective flags
  `-fopenmp -O3 -DNDEBUG`)
- compiler environment: `PrgEnv-cray/8.3.3`, Cray `CC` (CCE 13.0.2) with
  Cray MPICH 8.1.15, inherited from the default job environment
- source revision: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- workload: `-s 30`, `mpirun -np 1`
- resources for every job: `select=1:ncpus=8:mpiprocs=1:mem=16gb`, walltime
  `00:10:00`

## Controlled affinity environment

Held constant across all six jobs except the thread count:

| Variable | omp1 configuration | omp8 configuration |
| --- | --- | --- |
| `OMP_NUM_THREADS` | `1` | `8` |
| `OMP_PLACES` | `cores` | `cores` |
| `OMP_PROC_BIND` | `spread` | `spread` |
| `OMP_DISPLAY_AFFINITY` | `TRUE` | `TRUE` |

`OMP_DISPLAY_AFFINITY=TRUE` records the actual thread placement in the job
output. Affinity and oversubscription warnings are never suppressed; every
stderr file is preserved as evidence.

## Attempts and submission order

Submit alternately in the listed order; completion order may differ.

| Order | Wrapper | Experiment ID | Attempt | Threads | Job name | PBS outputs |
| --- | --- | --- | --- | ---: | --- | --- |
| 1 | `run_omp1_v1.pbs` | `CCE13-CrayMPICH8-s30-affinity-omp1` | `CCE13-CrayMPICH8-s30-affinity-omp1_v1` | 1 | `lulesh_cce13_aff_omp1_v1` | `outputs/CCE13-CrayMPICH8-s30-affinity-omp1_v1.o/.e` |
| 2 | `run_omp8_v1.pbs` | `CCE13-CrayMPICH8-s30-affinity-omp8` | `CCE13-CrayMPICH8-s30-affinity-omp8_v1` | 8 | `lulesh_cce13_aff_omp8_v1` | `outputs/CCE13-CrayMPICH8-s30-affinity-omp8_v1.o/.e` |
| 3 | `run_omp1_v1.1.pbs` | `CCE13-CrayMPICH8-s30-affinity-omp1` | `CCE13-CrayMPICH8-s30-affinity-omp1_v1.1` | 1 | `lulesh_cce13_aff_omp1_v1_1` | `outputs/CCE13-CrayMPICH8-s30-affinity-omp1_v1.1.o/.e` |
| 4 | `run_omp8_v1.1.pbs` | `CCE13-CrayMPICH8-s30-affinity-omp8` | `CCE13-CrayMPICH8-s30-affinity-omp8_v1.1` | 8 | `lulesh_cce13_aff_omp8_v1_1` | `outputs/CCE13-CrayMPICH8-s30-affinity-omp8_v1.1.o/.e` |
| 5 | `run_omp1_v1-final.pbs` | `CCE13-CrayMPICH8-s30-affinity-omp1` | `CCE13-CrayMPICH8-s30-affinity-omp1_v1-final` | 1 | `lulesh_cce13_aff_omp1_v1_final` | `outputs/CCE13-CrayMPICH8-s30-affinity-omp1_v1-final.o/.e` |
| 6 | `run_omp8_v1-final.pbs` | `CCE13-CrayMPICH8-s30-affinity-omp8` | `CCE13-CrayMPICH8-s30-affinity-omp8_v1-final` | 8 | `lulesh_cce13_aff_omp8_v1_final` | `outputs/CCE13-CrayMPICH8-s30-affinity-omp8_v1-final.o/.e` |

## Shared helper

Every wrapper calls `run_lulesh_cce13_affinity.sh` via `bash` with
`OMP_THREADS`, `EXPERIMENT_ID`, `ATTEMPT_SUFFIX`, and `REQUESTED_RESOURCES`.
The helper exports the controlled affinity environment, emits the metadata
required by `results/scripts/extract_lulesh_results.py` (experiment and
attempt IDs, PBS job ID, timestamp, hostname, binary, source commit, input
parameters, resources, module list, and launcher version), and runs only
`mpirun -np 1 <binary> -s 30`.

## Run attempts

Status: stopped after two completed jobs when Task-001's placement stop
condition was triggered. No further submissions, retries, or
affinity-configuration changes were made; the
remaining planned attempts (`..._v1.1`, `..._v1-final`) were not submitted.

Completed attempts:

| Attempt | PBS job | Node | Timestamp (UTC) | Threads | Elapsed (s) | FOM (z/s) | MaxRelDiff | Correctness | Run status |
| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- | --- |
| `CCE13-CrayMPICH8-s30-affinity-omp1_v1` | `25556314.pbs101` | `x1001c2s2b0n1` | `2026-09-25T22:56:19Z` | 1 | 15 | 1697.189 | `1.482369e-12` | passed (finite) | success |
| `CCE13-CrayMPICH8-s30-affinity-omp8_v1` | `25556332.pbs101` | `x1001c2s5b1n0` | `2026-09-25T22:59:23Z` | 8 | 8.1 | 3116.4855 | `1.461140e-12` | passed (finite) | success |

Both runs printed `Run completed:` with iteration count 932 and finite
correctness fields (omp1: `MaxAbsDiff=7.639755e-11`,
`TotalAbsDiff=8.590535e-10`; omp8: `MaxAbsDiff=6.548362e-11`,
`TotalAbsDiff=8.615093e-10`).

Thread-placement evidence from `OMP_DISPLAY_AFFINITY=TRUE` in stdout:

- omp1: thread 0 reports `affinity:  0`.
- omp8: all eight threads (0-7) report `affinity:  0`.

Preserved stderr evidence:

- omp1: one `[CCE OMP] affinity unbinding error: Invalid argument` message.
- omp8: the Cray oversubscription warning and eight
  `[CCE OMP] affinity unbinding error: Invalid argument` messages.

Raw evidence: `outputs/CCE13-CrayMPICH8-s30-affinity-omp1_v1.o/.e` and
`outputs/CCE13-CrayMPICH8-s30-affinity-omp8_v1.o/.e`.

## Result extraction record

The first extraction attempt with `results/scripts/extract_lulesh_results.py`
failed on both completed `.o` files with
`ValueError: Missing threads in extracted output`. With
`OMP_DISPLAY_AFFINITY=TRUE`, the Cray affinity report interrupts the
application's `Num threads:` line, so stdout contains
`Num threads: CCE OMP: host ... affinity:  0` with the thread count on the
next line, and the extractor's `Num threads:\s*([0-9]+)` pattern no longer
matches. All other fields parsed normally.

Track-1 repair, applied before the two rows were appended: the extractor now
prefers the run helper's explicit `openmp_threads:` metadata line and falls
back to the previous `Num threads:` application marker for older runs without
helper metadata. The `results/metrics.csv` schema is unchanged.

## RUNTIME error-patching record

No runtime error patching was performed. The affinity unbinding errors and
the omp8 oversubscription warning in the preserved stderr files are recorded
as evidence only; the controlled sequence was stopped instead of patched or
retried.
