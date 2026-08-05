# Intel-CrayMPICH8-smoke-s10 Run

## Summary

Run the one-rank LULESH `-s 10` smoke test with the successful Intel build and
the default Intel programming environment.

## Run configuration

- experiment ID: `Intel-CrayMPICH8-smoke-s10`
- build: `Intel-CrayMPICH8`
- input parameters: `-s 10`
- MPI tasks: `1`
- OpenMP threads: `1`
- compiler environment: `PrgEnv-intel/8.3.3`
- run resources: `select=1:ncpus=1:mpiprocs=1:mem=1gb`, walltime `00:10:00`
- PBS output directory: `outputs/`

## Run attempts

PBS `.o` and `.e` files in `outputs/` are the authoritative raw run records.

