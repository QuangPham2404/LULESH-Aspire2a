# CCE13-CrayMPICH8-baseline-s30-omp-sweep

Scale OpenMP threads using the existing CCE13 Release (`-O3 -DNDEBUG`) binary
with one MPI rank and `-s 30`. The one-thread baseline is already recorded in
the MPI-rank-1 result, so this sweep adds 8, 16, and 32 threads. No rebuild is
required.

| Experiment | MPI ranks | OpenMP threads | Resources |
| --- | ---: | ---: | --- |
| `CCE13-CrayMPICH8-baseline-s30-omp8` | 1 | 8 | `select=1:ncpus=8:mpiprocs=1:mem=16gb` |
| `CCE13-CrayMPICH8-baseline-s30-omp16` | 1 | 16 | `select=1:ncpus=16:mpiprocs=1:mem=16gb` |
| `CCE13-CrayMPICH8-baseline-s30-omp32` | 1 | 32 | `select=1:ncpus=32:mpiprocs=1:mem=16gb` |

- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0`
- effective flags: `-fopenmp -O3 -DNDEBUG`
- source revision: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`

## Run attempts

No run attempts have been submitted yet.

## RUNTIME error-patching record

No runtime errors recorded.
