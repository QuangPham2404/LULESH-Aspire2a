# LULESH Optimization Plan

## Scope and baseline

This plan optimizes the CCE13 configuration using the larger `-s 30`
workload. The selected baseline is:

- compiler: Cray CCE 13.0.2;
- MPI: Cray MPICH 8.1.15;
- source revision: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`;
- build: `Release`, with MPI and OpenMP enabled and SILO disabled;
- input: `-s 30`;
- MPI ranks: `1`;
- OpenMP threads: `1`;
- recorded elapsed time: `20 s`;
- recorded FOM: `1281.9581 z/s`;
- correctness: passed, with `MaxRelDiff = 1.482369e-12`.

The previous `-s 30` environment comparison identified CCE13 as the fastest
valid result. The Intel result is excluded from optimization comparisons
because it reported `MaxRelDiff = -nan`.

## Important Release-build finding

The current CCE13 CMake `Release` configuration already injects:

```text
-O3 -DNDEBUG
```

With OpenMP enabled, the generated compile flags are:

```text
-fopenmp -O3 -DNDEBUG
```

Consequently, the existing CCE13 Release binary is the `-O3` case. Any new
optimization build must use a separate build directory and must record the
actual generated flags, so that results are not confused with the existing
baseline.

## Experimental procedure

### 1. Establish timing stability

Repeat the CCE13 baseline with `-s 30`, one MPI rank, and one OpenMP thread.
Use the same source revision, binary, modules, PBS resources, and input for
all repetitions. Retain every attempt as a separate result row. Because
LULESH currently reports elapsed time in whole seconds, use multiple
repetitions to reduce timing noise and record any available higher-resolution
timing as supplementary metadata.

### 2. Compare compiler optimization levels

Build and run three explicit CCE13 variants:

| Variant | Required effective optimization |
| --- | --- |
| CCE13-O2 | `-O2 -DNDEBUG` |
| CCE13-O3 | `-O3 -DNDEBUG` |
| CCE13-Ofast | `-Ofast -DNDEBUG` |

Run every variant with:

```text
problem size: -s 30
MPI ranks: 1
OpenMP threads: 1
```

The `-O3` result is the direct comparison against the existing Release
baseline. The `-Ofast` result requires special scientific-accuracy review,
because fast-math transformations may change floating-point behavior.

For every variant, record the compiler command flags, runtime, FOM, iteration
count, final energy, `MaxAbsDiff`, `TotalAbsDiff`, `MaxRelDiff`, and all
correctness/convergence markers. A variant is performance-valid only when its
correctness fields are finite and pass the applicable acceptance checks.

Select the fastest valid optimization level after repeated measurements. If
`-Ofast` changes results beyond the accepted tolerance or produces a failed or
non-finite correctness marker, preserve the result but exclude it from the
valid winner selection.

### 3. Scale MPI ranks

Using the selected optimization build from step 2, keep OpenMP threads fixed
at one and test:

| MPI ranks | OpenMP threads |
| ---: | ---: |
| 1 | 1 |
| 8 | 1 |
| 27 | 1 |

Keep `-s 30`, compiler environment, binary, and correctness criteria fixed.
Request and record resources appropriate to the total MPI ranks, and record
rank placement, allocated node(s), and binding information. The 27-rank case
is compatible with a three-dimensional decomposition of a size-30 problem.

Select the fastest valid MPI-rank configuration using repeated measurements.

### 4. Scale OpenMP threads

Using the selected optimization build and MPI-rank configuration from step 3,
test:

| MPI ranks | OpenMP threads |
| ---: | ---: |
| selected | 1 |
| selected | 8 |
| selected | 16 |
| selected | 32 |

Set and record `OMP_NUM_THREADS` explicitly. Ensure PBS CPU requests and
process/thread binding match the requested configuration. Record total
logical execution resources as:

```text
MPI ranks x OpenMP threads
```

Select the fastest valid hybrid configuration after repeated measurements.

### 5. Confirm the final selection

Repeat the selected final configuration under the same resource and
environment conditions. Confirm that the speedup is reproducible and that the
correctness fields remain acceptable. Do not replace the baseline record;
retain the baseline and every intermediate attempt for comparison.

## Selection criteria

Configurations are ranked in this order:

1. correctness and convergence must pass;
2. all required numerical fields must be finite;
3. numerical results must remain within the accepted tolerance relative to the
   CCE13 baseline/reference;
4. among valid configurations, select the lowest stable LULESH elapsed time;
5. use FOM as a supporting performance metric, not as a substitute for
   correctness.

Every build and run must preserve the experiment ID, attempt label, PBS job
ID, timestamps, allocated host, compiler and MPI versions, loaded modules,
effective build flags, input, requested resources, runtime, correctness
fields, stdout/stderr paths, exit status, and binary path.

## Results handling

Use the existing `results/metrics.csv` schema. Append each repeated
measurement as a separate row and regenerate `results/RESULTS.md` from the
CSV. Preserve failed or scientifically invalid attempts with their actual
status; do not silently discard them. Optimization conclusions belong in
this planning document only after the corresponding validated results have
been recorded.

## Current next step

Prepare the separate CCE13 `-O2`, `-O3`, and `-Ofast` build/run cases after
recording the repeated CCE13 Release baseline timing.
