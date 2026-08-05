# AOCC-CrayMPICH8-baseline-s30 Run

## Summary

Run the existing successful AOCC Release build with one MPI rank, one OpenMP
thread, and the larger `-s 30` baseline input. This case reuses the completed
AOCC build; it does not rebuild the application.

## Run configuration

- experiment ID: `AOCC-CrayMPICH8-baseline-s30`
- build: `AOCC-CrayMPICH8`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-AOCC-CrayMPICH8-Release/lulesh2.0`
- source commit: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- input parameters: `-s 30`
- MPI tasks: `1`
- OpenMP threads: `1`
- command: `mpirun -np 1 <successful-build-binary> -s 30`
- compiler environment: `PrgEnv-aocc/8.3.3`
- compiler: AOCC CC 3.2.0
- MPI: Cray MPICH 8.1.15
- build flags: `Release; WITH_MPI=On; WITH_OPENMP=On; WITH_SILO=Off`
- run resources: `select=1:ncpus=1:mpiprocs=1:mem=16gb`, walltime `00:10:00`
- PBS output directory: `outputs/`

## Run attempts

### AOCC-CrayMPICH8-baseline-s30_v1

- Status: success
- PBS job ID: `15093830.pbs101`
- PBS state: `F`
- PBS exit status: `0`
- Timestamp: `2026-08-05T10:43:20Z`
- Hostname/node: `x1003c2s1b1n1`
- PBS walltime: `00:00:48`
- PBS stdout: `outputs/AOCC-CrayMPICH8-baseline-s30_v1.o`
- PBS stderr: `outputs/AOCC-CrayMPICH8-baseline-s30_v1.e`
- Problem size: `30`
- MPI tasks: `1`
- OpenMP threads: `1`
- Iterations: `932`
- Final Origin Energy: `2.025075e+05`
- MaxAbsDiff: `7.639755e-11`
- TotalAbsDiff: `8.590535e-10`
- MaxRelDiff: `1.482369e-12`
- LULESH elapsed time: `32 s`
- FOM: `778.03348 z/s`
- Correctness: passed; expected output and finite correctness fields were present.
- Observed error: none

## Runtime error-patching record

No runtime errors recorded yet.
