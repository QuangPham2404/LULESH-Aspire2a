# CCE13-CrayMPICH8-baseline-s30 Run

## Summary

Run the existing successful CCE Release build with one MPI rank, one OpenMP
thread, and the larger `-s 30` baseline input. This case reuses the completed
CCE build; it does not rebuild the application.

## Run configuration

- experiment ID: `CCE13-CrayMPICH8-baseline-s30`
- build: `CCE13-CrayMPICH8-newWF`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0`
- source commit: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- input parameters: `-s 30`
- MPI tasks: `1`
- OpenMP threads: `1`
- command: `mpirun -np 1 <successful-build-binary> -s 30`
- compiler environment: `PrgEnv-cray/8.3.3`
- compiler: Cray CC 13.0.2
- MPI: Cray MPICH 8.1.15
- build flags: `Release; WITH_MPI=On; WITH_OPENMP=On; WITH_SILO=Off`
- run resources: `select=1:ncpus=1:mpiprocs=1:mem=16gb`, walltime `00:10:00`
- PBS output directory: `outputs/`

## Run attempts

### CCE13-CrayMPICH8-baseline-s30_v1

- Status: success
- PBS job ID: `15093829.pbs101`
- PBS state: `F`
- PBS exit status: `0`
- Timestamp: `2026-08-05T10:43:19Z`
- Hostname/node: `x1003c2s1b1n1`
- PBS walltime: `00:00:26`
- PBS stdout: `outputs/CCE13-CrayMPICH8-baseline-s30_v1.o`
- PBS stderr: `outputs/CCE13-CrayMPICH8-baseline-s30_v1.e`
- Problem size: `30`
- MPI tasks: `1`
- OpenMP threads: `1`
- Iterations: `932`
- Final Origin Energy: `2.025075e+05`
- MaxAbsDiff: `7.639755e-11`
- TotalAbsDiff: `8.590535e-10`
- MaxRelDiff: `1.482369e-12`
- LULESH elapsed time: `20 s`
- FOM: `1281.9581 z/s`
- Correctness: passed; expected output and finite correctness fields were present.
- Observed error: none

## Runtime error-patching record

No runtime errors recorded yet.
