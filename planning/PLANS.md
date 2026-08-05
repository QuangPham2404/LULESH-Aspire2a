# LULESH Optimization Plans

## Completed Optimization Steps

- Established the application overview, source revision, baseline build/run
  workflow, and correctness markers for LULESH source revision
  `3e01c40b3281aadb7f996525cdd4a3354f6d3801`.
- Completed a one-rank, one-thread `-s 10` programming-environment sweep using
  Cray CCE 13.0.2, AOCC 3.2.0, GNU 11.2.0, and Intel 2024.0 with Cray MPICH
  8.1.15.
- Confirmed correctness for the CCE, AOCC, and GNU runs.
- Recorded the Intel run as completed but correctness-failed because
  `MaxRelDiff = -nan`. It must not be treated as a valid performance result.
- Established AOCC as the current fastest valid environment in the recorded
  smoke runs: `0.26 s` and `895.58097 z/s`.
- Established that the current measurements are single samples from a very
  small one-rank workload and are not yet sufficient for strong performance
  conclusions.

## Current Optimization Plan

### Executive summary of plan
Build a repeatable workflow for compiling, running, validating, and optimizing
LULESH on Aspire2A, then characterize the effects of compiler, OpenMP, MPI, and
hybrid parallel configurations.

### Detailed steps

1. Establish a stable valid baseline.
   - Use the AOCC build as the primary baseline candidate because it is
     currently the fastest valid environment.
   - Retain CCE and GNU as comparison baselines.
   - Increase the problem size from `-s 10` to a larger controlled size such
     as `-s 30` so runtime measurements are less dominated by startup and
     scheduler noise.
   - Repeat each baseline configuration several times with one MPI task and
     one OpenMP thread.
   - Keep the source revision, Release build, input, and requested resources
     fixed while repeating measurements.

2. Measure OpenMP scaling with the AOCC baseline.
   - Keep one MPI task and the same binary and problem size.
   - Test a controlled thread series such as `OMP_NUM_THREADS=1,2,4,8,16,32`.
   - Record runtime, FOM, correctness, node allocation, and all environment
     metadata for every thread count.

3. Compare MPI and hybrid parallelism.
   - Compare equivalent configurations such as one MPI task with many
     threads, multiple MPI tasks with fewer threads, and MPI-only layouts.
   - Keep total resources and problem size controlled so the comparison tests
     parallel layout rather than unrelated resource changes.
   - Use the Aspire2A hardware information, including its 128 physical cores
     and eight NUMA nodes, to guide later single-node placement experiments.

4. Compare compiler optimization flags.
   - First verify the actual compiler flags emitted by the current CMake
     `Release` configuration.
   - Test flag variants one compiler at a time, beginning with AOCC.
   - Start with conservative versus higher optimization levels, then test
     supported AMD EPYC 7713 architecture-specific tuning.
   - Treat each flag variant as a separate build and run experiment.
   - Require correctness validation for every variant; timing alone cannot
     establish a successful optimization.

5. Investigate Intel correctness separately before using Intel for performance
   comparisons.
   - Preserve the existing Intel result as a completed,
     correctness-failed record.
   - Do not use its faster runtime or FOM as an optimization conclusion while
     `MaxRelDiff` remains non-finite.
   - Any future Intel work should first be a correctness investigation and
     should follow the scientific-correctness reporting procedure.

## Results and Analysis

The current results contain four one-rank, one-thread `-s 10` runs:

| Environment | Elapsed (s) | FOM (z/s) | Correctness |
| --- | ---: | ---: | --- |
| Cray CCE 13.0.2 | 0.35 | 656.99887 | passed |
| AOCC 3.2.0 | 0.26 | 895.58097 | passed |
| GNU 11.2.0 | 0.34 | 682.15817 | passed |
| Intel 2024.0 | 0.20 | 1182.5021 | failed (`MaxRelDiff = -nan`) |

AOCC is the current fastest valid result, but the data is limited to one
measurement per environment and a very small workload. The next measurements
must establish repeatability and a more representative runtime before drawing
optimization conclusions.

## Next Step

Run a repeated larger-problem AOCC baseline with one MPI task and one OpenMP
thread, then use the same AOCC build for an OpenMP thread-scaling sweep. Keep
the existing results schema unless a future experiment requires new columns,
units, or result semantics.
