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

### Initial attempts

All three initial jobs failed before application startup because the wrapper
could not find the shared runner through a relative path:

- `CCE13-CrayMPICH8-baseline-s30-mpi1_v1`, PBS job `15097036.pbs101`, stderr
  `outputs/CCE13-CrayMPICH8-baseline-s30-mpi1_v1.e`;
- `CCE13-CrayMPICH8-baseline-s30-mpi8_v1`, PBS job `15097037.pbs101`, stderr
  `outputs/CCE13-CrayMPICH8-baseline-s30-mpi8_v1.e`;
- `CCE13-CrayMPICH8-baseline-s30-mpi27_v1`, PBS job `15097038.pbs101`, stderr
  `outputs/CCE13-CrayMPICH8-baseline-s30-mpi27_v1.e`.

Observed error: `./run_lulesh_cce13_mpi.pbs: No such file or directory` and
PBS exit status `127`. Suspected cause: compute-node working-directory
resolution differed from the qsub submission path. Patch: invoke the shared
runner through its absolute project-root path and use new `v1.1` output names.

Retry attempts are pending.

## RUNTIME error-patching record

No runtime errors recorded.
