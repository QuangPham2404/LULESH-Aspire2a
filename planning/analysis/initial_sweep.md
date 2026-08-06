# Analysis: Initial `-s 30` Sweep

## 1. Concise summary

This analysis groups all recorded runtime results in `results/metrics.csv`
using the `-s 30` input into four optimization directions:

1. compiler/PrgEnv comparison;
2. explicit CCE13 optimization flags;
3. MPI-rank scaling for the previous valid CCE13 configuration; and
4. OpenMP-thread scaling for the previous valid CCE13 configuration.

The comparison uses correctness-first selection. A result with a failed or
non-finite correctness field is retained as evidence but is not eligible to be
selected as a valid optimization winner.

## 2. Scope and evaluation criteria

- Analysis ID: `initial_sweep`
- Analysis date: 2026-08-06
- Source: [`results/metrics.csv`](../../results/metrics.csv)
- Workload: `-s 30`
- Source revision for all rows: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- MPI implementation: Cray MPICH 8.1.15
- Selection baseline: CCE13 Release with MPI/OpenMP enabled and SILO
  disabled, effective optimization `-O3 -DNDEBUG`, one MPI rank, and one
  OpenMP thread.
- Baseline row: `CCE13-CrayMPICH8-baseline-s30_v1`, 20 s, FOM 1281.9581,
  correctness passed.
- Primary performance metric: LULESH elapsed time in seconds.
- Supporting metric: LULESH FOM in zones/second.
- Validity requirements: `correctness_status=passed`, finite correctness
  fields, and `run_status=success`.

Each selected row is a single recorded runtime attempt. These are directional
measurements, not repeated statistical samples. The reported LULESH elapsed
times are mostly whole seconds, so timing stability and affinity must be
controlled before treating small differences as reproducible.

## 3. Data and analysis

### 3.1 Compiler/PrgEnv sweep

These rows compare the available compiler environments at the same `-s 30`,
one-rank, one-thread configuration.

| Compiler environment | Experiment / attempt | Elapsed (s) | FOM (z/s) | Correctness | Run status |
| --- | --- | ---: | ---: | --- | --- |
| CCE13 / PrgEnv-cray | `CCE13-CrayMPICH8-baseline-s30` / `..._v1` | 20 | 1281.9581 | passed | success |
| AOCC / PrgEnv-aocc | `AOCC-CrayMPICH8-baseline-s30` / `..._v1` | 32 | 778.03348 | passed | success |
| Intel / PrgEnv-intel | `Intel-CrayMPICH8-baseline-s30` / `..._v1` | 25 | 1019.1226 | failed (`MaxRelDiff=-nan`) | success |
| GNU / PrgEnv-gnu | `GNU-CrayMPICH8-baseline-s30` / `..._v1` | 27 | 941.23381 | passed | success |

CCE13 is the fastest valid environment in this recorded comparison. AOCC is
60% slower than CCE13 by elapsed time, and GNU is 35% slower. Intel is faster
than AOCC and GNU but cannot be selected because its relative-difference field
is non-finite. This sweep supports selecting CCE13 as the environment for the
subsequent optimization-direction tests, subject to repeat measurements.

### 3.2 CCE13 optimization-flag sweep

The following tests use CCE13, one MPI rank, and one OpenMP thread. The
existing Release baseline is the effective `-O3` case.

| Effective flags | Experiment / attempt | Elapsed (s) | FOM (z/s) | Correctness | Run status |
| --- | --- | ---: | ---: | --- | --- |
| `-O3 -DNDEBUG` | `CCE13-CrayMPICH8-baseline-s30` / `..._v1` | 20 | 1281.9581 | passed | success |
| `-O2 -DNDEBUG` | `CCE13-CrayMPICH8-O2-s30` / `..._v1` | 22 | 1167.0982 | passed | success |
| `-Ofast -DNDEBUG` | `CCE13-CrayMPICH8-Ofast-s30` / `..._v1` | 17 | 1484.2957 | failed (`MaxRelDiff=-nan`) | success |

`-O2` is valid but approximately 10% slower than the CCE13 baseline. `-Ofast`
is approximately 15% faster in the recorded measurement, but its non-finite
correctness field makes it scientifically invalid for winner selection. The
valid flag selection therefore remains `-O3 -DNDEBUG`. The `-Ofast` result is
not discarded; it is a correctness investigation candidate only if such an
investigation is explicitly authorized later.

### 3.3 MPI-rank scaling for the previous valid configuration

These runs reuse the CCE13 Release/O3 binary and keep one OpenMP thread per
MPI rank.

| MPI ranks | Experiment / attempt | Elapsed (s) | FOM (z/s) | Correctness | Requested resources |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | `CCE13-CrayMPICH8-baseline-s30-mpi1` / `..._v1` | 20 | 1258.0879 | passed | 1 rank, 1 CPU |
| 8 | `CCE13-CrayMPICH8-baseline-s30-mpi8` / `..._v1` | 70 | 6230.7687 | passed | 8 ranks, 8 CPUs |
| 27 | `CCE13-CrayMPICH8-baseline-s30-mpi27` / `..._v1` | 170 | 13372.882 | passed | 27 ranks, 27 CPUs |

The FOM increases with rank count, but elapsed time also increases. This is
not a strong-scaling result: LULESH interprets `-s 30` per MPI domain, so the
total work increases as the number of MPI domains increases. The results are
therefore useful as weak-scaling-style observations, not evidence that adding
MPI ranks accelerates a fixed global problem size. The one-rank repeated
baseline is close in elapsed time to the original baseline, but its FOM differs
slightly; this reinforces the need for repeated measurements under controlled
conditions.

### 3.4 OpenMP-thread scaling for the previous valid configuration

These runs use one MPI rank and the CCE13 Release/O3 binary.

| MPI ranks x OpenMP threads | Experiment / attempt | Elapsed (s) | FOM (z/s) | Correctness |
| --- | --- | ---: | ---: | --- |
| 1 x 1 | `CCE13-CrayMPICH8-baseline-s30-mpi1` / `..._v1` | 20 | 1258.0879 | passed |
| 1 x 8 | `CCE13-CrayMPICH8-baseline-s30-omp8` / `..._v1` | 6.6 | 3784.5446 | passed |
| 1 x 16 | `CCE13-CrayMPICH8-baseline-s30-omp16` / `..._v1` | 17 | 1470.1691 | passed |
| 1 x 32 | `CCE13-CrayMPICH8-baseline-s30-omp32` / `..._v1` | 31 | 806.53914 | passed |

The 8-thread run is the fastest measured valid configuration, with a recorded
elapsed-time improvement of about 3.0x over the one-thread run. Performance
then regresses at 16 and 32 threads. All three OpenMP sweep stderr files
contain a Cray warning that the requested thread count or affinity may
oversubscribe available CPU resources. Consequently, the 8-thread result is
the current measured candidate, not yet a stable final selection. No affinity
or resource-policy change was applied during this analysis.

## 4. Insights gained

- CCE13 is the fastest valid compiler environment in the recorded `-s 30`
  comparison.
- Within the tested CCE13 flags, `-O3` is the fastest valid configuration.
- `-Ofast` cannot be selected despite its lower runtime because it reports a
  non-finite correctness value.
- The MPI sweep does not measure fixed-global-size scaling. Its higher FOM at
  higher rank counts reflects increased total work as well as parallel
  execution.
- The OpenMP sweep identifies 8 threads as the strongest measured candidate,
  but the affinity/oversubscription warning weakens the conclusion.
- Every optimization-direction comparison currently has only one runtime row
  per configuration. No reliable variance estimate or repeatability claim can
  be made.
- The existing records are sufficient to choose a provisional direction, but
  not sufficient to claim a final, reproducible optimum.

## 5. Suggested next section

The next optimization section should first establish stable measurements for
the current candidate rather than immediately changing compiler flags or
source code.

Suggested direction: controlled affinity and repeatability validation of the
CCE13 Release/O3 configurations, especially `1 MPI rank x 8 OpenMP threads`.

The next section should:

- determine and explicitly record the valid CPU/thread placement for 1, 8, 16,
  and 32 OpenMP threads;
- repeat the one-thread baseline and 8-thread candidate under identical
  resource and affinity conditions;
- retain all repetitions as separate result rows;
- confirm finite correctness fields for every repetition; and
- only then confirm or reject the 8-thread configuration as the stable final
  measured selection.

A separate later direction may test fixed-global-size MPI strong scaling if
that question is important. The current MPI rows should not be used to answer
that question.

## 6. Provenance

- Source data: [`results/metrics.csv`](../../results/metrics.csv)
- Generated report: [`results/RESULTS.md`](../../results/RESULTS.md)
- Source revision: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- Common environment: Cray MPICH 8.1.15 and launcher version 1.1.6
- All included rows have `run_status=success`; Intel baseline and CCE13
  `-Ofast` have `correctness_status=failed` and remain included as invalid
  evidence.

Raw stdout/stderr paths are recorded in the corresponding CSV rows and in
`results/RESULTS.md`. The grouped experiment directories are:

- [`experiments/CCE13-CrayMPICH8-baseline-s30/`](../../experiments/CCE13-CrayMPICH8-baseline-s30/)
- [`experiments/AOCC-CrayMPICH8-baseline-s30/`](../../experiments/AOCC-CrayMPICH8-baseline-s30/)
- [`experiments/Intel-CrayMPICH8-baseline-s30/`](../../experiments/Intel-CrayMPICH8-baseline-s30/)
- [`experiments/GNU-CrayMPICH8-baseline-s30/`](../../experiments/GNU-CrayMPICH8-baseline-s30/)
- [`experiments/CCE13-CrayMPICH8-O2-s30/`](../../experiments/CCE13-CrayMPICH8-O2-s30/)
- [`experiments/CCE13-CrayMPICH8-Ofast-s30/`](../../experiments/CCE13-CrayMPICH8-Ofast-s30/)
- [`experiments/CCE13-CrayMPICH8-baseline-s30-mpi-sweep/`](../../experiments/CCE13-CrayMPICH8-baseline-s30-mpi-sweep/)
- [`experiments/CCE13-CrayMPICH8-baseline-s30-omp-sweep/`](../../experiments/CCE13-CrayMPICH8-baseline-s30-omp-sweep/)
