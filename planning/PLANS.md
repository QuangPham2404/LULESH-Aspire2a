# LULESH Optimization Plan — Master Tracker

This file is the concise tracker for optimization directions. Detailed data,
interpretation, limitations, and proposed follow-ups are stored in the linked
files under [`planning/analysis/`](analysis/).

## Current baseline

- Environment: Cray CCE 13.0.2 / Cray MPICH 8.1.15
- Source revision: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- Build: Release, MPI/OpenMP enabled, SILO disabled; effective `-O3 -DNDEBUG`
- Workload: `-s 30`
- Baseline configuration: 1 MPI rank x 1 OpenMP thread
- Baseline measurement: 20 s, FOM 1281.9581, correctness passed

## Optimization directions

| Direction | Analysis | Status | Main finding | Suggested follow-up |
| --- | --- | --- | --- | --- |
| Compiler/PrgEnv comparison | [`initial_sweep.md`](analysis/initial_sweep.md#31-compilerprgenv-sweep) | analyzed, provisional | CCE13 is the fastest valid environment; Intel is scientifically invalid due to `MaxRelDiff=-nan` | Repeat under controlled timing before final ranking |
| CCE13 optimization flags | [`initial_sweep.md`](analysis/initial_sweep.md#32-cce13-optimization-flag-sweep) | analyzed, provisional | `-O3` is the fastest valid tested flag; `-Ofast` is faster but invalid | Preserve `-O3`; investigate `-Ofast` only with explicit correctness authorization |
| CCE13 MPI scaling | [`initial_sweep.md`](analysis/initial_sweep.md#33-mpi-rank-scaling-for-the-previous-valid-configuration) | analyzed, scope-limited | Higher ranks increase FOM and elapsed time for per-domain `-s 30`; this is weak-scaling-style data | Use fixed global size for a separate strong-scaling study if required |
| CCE13 OpenMP scaling | [`initial_sweep.md`](analysis/initial_sweep.md#34-openmp-thread-scaling-for-the-previous-valid-configuration) | analyzed, provisional | 8 threads is the fastest measured valid configuration, but affinity warnings remain | Control affinity and repeat 1-thread and 8-thread cases |

## Immediate next direction

Validate timing stability and CPU/thread affinity for the CCE13 Release/O3
baseline and the 1 MPI rank x 8 OpenMP thread candidate. Do not treat the
current single measurements as a final reproducible optimum until the warning
and repeatability questions are addressed.

## Analysis history

| Analysis ID | Date | Scope | Source |
| --- | --- | --- | --- |
| `initial_sweep` | 2026-08-06 | All recorded `-s 30` runtime rows grouped into four directions | [`results/metrics.csv`](../results/metrics.csv) |
