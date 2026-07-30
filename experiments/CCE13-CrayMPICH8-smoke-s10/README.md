# Experiment: CCE13-CrayMPICH8-smoke-s10

## Purpose

Smoke test the baseline `CCE13-CrayMPICH8` LULESH build with one MPI rank and a
small problem size.

## Metadata

- Experiment ID: `CCE13-CrayMPICH8-smoke-s10`
- PBS job ID: `15032369.pbs101`
- Timestamp: `2026-07-30T00:37:36Z`
- Hostname/node: `x1003c4s5b0n1`
- Build category: `CCE13-CrayMPICH8`
- Binary:
  `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH/build-CCE13-CrayMPICH8-Release/lulesh2.0`
- Compiler and version: Cray CCE 13.0.2 through `CC`
- MPI implementation and version: Cray MPICH 8.1.15
- Loaded module baseline: `PrgEnv-cray/8.3.3`, `cce/13.0.2`,
  `cray-mpich/8.1.15`
- Input parameters: `-s 10`
- Requested resources: 1 node, 1 MPI rank, 1 CPU, 1 GB memory, 10 minutes
- stdout path: `smoke_s10_v1.o`
- stderr path: `smoke_s10_v1.e`
- Exit status: `0`
- Runtime: 0.28 seconds reported by LULESH; 7 seconds PBS walltime
- Correctness result: passed LULESH energy-difference checks

## Attempts

### v1

- PBS job ID: `15032369.pbs101`
- Status: success
- stdout: `smoke_s10_v1.o`
- stderr: `smoke_s10_v1.e`
- Command: `mpirun -np 1 <binary> -s 10`
- Validation criteria:
  - PBS exit status is 0: passed.
  - LULESH reports normal problem setup/output: passed.
  - LULESH prints final elapsed time/performance output: passed.
- Observed output:
  - Problem size: 10
  - MPI tasks: 1
  - Iteration count: 231
  - Final Origin Energy: `2.720531e+04`
  - MaxAbsDiff: `2.273737e-12`
  - TotalAbsDiff: `1.659646e-11`
  - MaxRelDiff: `4.649603e-14`
  - Elapsed time: 0.28 seconds
  - FOM: `833.13504 z/s`
