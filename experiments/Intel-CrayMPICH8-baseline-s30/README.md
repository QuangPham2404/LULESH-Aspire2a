# Intel-CrayMPICH8-baseline-s30 Run

## Summary

Run the existing Intel Release build with one MPI rank, one OpenMP thread, and
the larger `-s 30` baseline input. This case reuses the completed Intel build;
it does not rebuild the application. The previous Intel `-s 10` run had a
non-finite correctness result, so this run must be reported with correctness
validation independently of runtime completion.

## Run configuration

- experiment ID: `Intel-CrayMPICH8-baseline-s30`
- build: `Intel-CrayMPICH8`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-Intel-CrayMPICH8-Release/lulesh2.0`
- source commit: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- input parameters: `-s 30`
- MPI tasks: `1`
- OpenMP threads: `1`
- command: `mpirun -np 1 <successful-build-binary> -s 30`
- compiler environment: `PrgEnv-intel/8.3.3`
- compiler: Intel CC 2024.0
- MPI: Cray MPICH 8.1.15
- build flags: `Release; WITH_MPI=On; WITH_OPENMP=On; WITH_SILO=Off`
- run resources: `select=1:ncpus=1:mpiprocs=1:mem=16gb`, walltime `00:10:00`
- PBS output directory: `outputs/`

## Run attempts

### Intel-CrayMPICH8-baseline-s30_v1

- Status: success; correctness failed
- PBS job ID: `15093831.pbs101`
- PBS state: `F`
- PBS exit status: `0`
- Timestamp: `2026-08-05T10:43:21Z`
- Hostname/node: `x1001c2s7b1n0`
- PBS walltime: `00:00:35`
- PBS stdout: `outputs/Intel-CrayMPICH8-baseline-s30_v1.o`
- PBS stderr: `outputs/Intel-CrayMPICH8-baseline-s30_v1.e`
- Problem size: `30`
- MPI tasks: `1`
- OpenMP threads: `1`
- Iterations: `932`
- Final Origin Energy: `2.025075e+05`
- MaxAbsDiff: `4.365575e-11`
- TotalAbsDiff: `7.966711e-10`
- MaxRelDiff: `-nan`
- LULESH elapsed time: `25 s`
- FOM: `1019.1226 z/s`
- Correctness: failed because `MaxRelDiff` was non-finite; no patch was attempted.
- Observed error: repeated Intel correctness failure from the prior `-s 10` run.

## Runtime error-patching record

No runtime errors recorded yet.
