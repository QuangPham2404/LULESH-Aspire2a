# Experiment: CCE13-CrayMPICH8-smoke-s10

## Purpose

Smoke test the baseline `CCE13-CrayMPICH8` LULESH build with one MPI rank and a
small problem size.

## Metadata

- Experiment ID: `CCE13-CrayMPICH8-smoke-s10`
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

## Attempts

### v1

- PBS job ID:
- Status: pending
- stdout: `smoke_s10_v1.o`
- stderr: `smoke_s10_v1.e`
- Command: `mpirun -np 1 <binary> -s 10`
- Validation criteria:
  - PBS exit status is 0.
  - LULESH reports normal problem setup/output.
  - LULESH prints final elapsed time/performance output.
