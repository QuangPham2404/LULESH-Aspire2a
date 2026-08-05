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

- Status: pending submission
- PBS stdout: `outputs/GNU-CrayMPICH8-baseline-s30_v1.o`
- PBS stderr: `outputs/GNU-CrayMPICH8-baseline-s30_v1.e`
- Expected correctness markers: `Run completed:`, `MaxRelDiff`, `Elapsed time`, and `FOM`

## Runtime error-patching record

No runtime errors recorded yet.
