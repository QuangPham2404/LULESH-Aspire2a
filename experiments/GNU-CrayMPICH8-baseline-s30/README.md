# GNU-CrayMPICH8-baseline-s30 Run

## Summary

Run the existing successful GNU Release build with one MPI rank, one OpenMP
thread, and the larger `-s 30` baseline input. This case reuses the completed
GNU build; it does not rebuild the application.

## Run configuration

- experiment ID: `GNU-CrayMPICH8-baseline-s30`
- build: `GNU-CrayMPICH8`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-GNU-CrayMPICH8-Release/lulesh2.0`
- source commit: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- input parameters: `-s 30`
- MPI tasks: `1`
- OpenMP threads: `1`
- command: `mpirun -np 1 <successful-build-binary> -s 30`
- compiler environment: `PrgEnv-gnu/8.3.3`
- compiler: GNU CC 11.2.0
- MPI: Cray MPICH 8.1.15
- build flags: `Release; WITH_MPI=On; WITH_OPENMP=On; WITH_SILO=Off`
- run resources: `select=1:ncpus=1:mpiprocs=1:mem=16gb`, walltime `00:10:00`
- PBS output directory: `outputs/`

## Run attempts

### GNU-CrayMPICH8-baseline-s30_v1

- Status: success
- PBS job ID: `15093832.pbs101`
- PBS state: `F`
- PBS exit status: `0`
- Timestamp: `2026-08-05T10:43:21Z`
- Hostname/node: `x1001c2s7b1n0`
- PBS walltime: `00:00:31`
- PBS stdout: `outputs/GNU-CrayMPICH8-baseline-s30_v1.o`
- PBS stderr: `outputs/GNU-CrayMPICH8-baseline-s30_v1.e`
- Problem size: `30`
- MPI tasks: `1`
- OpenMP threads: `1`
- Iterations: `932`
- Final Origin Energy: `2.025075e+05`
- MaxAbsDiff: `6.184564e-11`
- TotalAbsDiff: `7.360500e-10`
- MaxRelDiff: `1.369973e-12`
- LULESH elapsed time: `27 s`
- FOM: `941.23381 z/s`
- Correctness: passed; expected output and finite correctness fields were present.
- Observed error: none

## Runtime error-patching record

No runtime errors recorded yet.
