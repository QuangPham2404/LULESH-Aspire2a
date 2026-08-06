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

### Corrected retry attempts

- `CCE13-CrayMPICH8-baseline-s30-mpi1_v1`, PBS job `15097040.pbs101`, node
  `x1001c6s0b1n1`, completed `F / 0`; elapsed `20 s`, FOM `1258.0879`,
  correctness passed.
- `CCE13-CrayMPICH8-baseline-s30-mpi8_v1`, PBS job `15097041.pbs101`, node
  `x1002c5s2b0n0`, completed `F / 0`; elapsed `70 s`, FOM `6230.7687`,
  correctness passed.
- `CCE13-CrayMPICH8-baseline-s30-mpi27_v1`, PBS job `15097042.pbs101`, node
  `x1001c0s0b0n0`, completed `F / 0`; elapsed `170 s`, FOM `13372.882`,
  correctness passed.

All corrected retries reported finite correctness fields. With `-s 30` per
MPI domain, total work increases with MPI rank count; these measurements are
weak-scaling-style results rather than fixed-global-size strong scaling.

## RUNTIME error-patching record

No runtime errors recorded.
