# CCE13-CrayMPICH8-baseline-s30-mpi-sweep

Scale the existing CCE13 Release (`-O3 -DNDEBUG`) binary at problem size
`-s 30` with one OpenMP thread per MPI rank. No rebuild is required.

| Experiment | MPI ranks | OpenMP threads | Resources |
| --- | ---: | ---: | --- |
| `CCE13-CrayMPICH8-baseline-s30-mpi1` | 1 | 1 | `select=1:ncpus=1:mpiprocs=1:mem=16gb` |
| `CCE13-CrayMPICH8-baseline-s30-mpi8` | 8 | 1 | `select=1:ncpus=8:mpiprocs=8:mem=16gb` |
| `CCE13-CrayMPICH8-baseline-s30-mpi27` | 27 | 1 | `select=1:ncpus=27:mpiprocs=27:mem=16gb` |

- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0`
- effective flags: `-fopenmp -O3 -DNDEBUG`
- source revision: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`

## Run attempts

No run attempts have been submitted yet.

## RUNTIME error-patching record

No runtime errors recorded.
