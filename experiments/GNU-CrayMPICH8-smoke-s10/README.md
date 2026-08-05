# GNU-CrayMPICH8-smoke-s10 Run

## Summary

Run the one-rank LULESH `-s 10` smoke test with the successful GNU build and
the default GNU programming environment.

## Run configuration

- experiment ID: `GNU-CrayMPICH8-smoke-s10`
- build: `GNU-CrayMPICH8`
- input parameters: `-s 10`
- MPI tasks: `1`
- OpenMP threads: `1`
- compiler environment: `PrgEnv-gnu/8.3.3`
- run resources: `select=1:ncpus=1:mpiprocs=1:mem=1gb`, walltime `00:10:00`
- PBS output directory: `outputs/`

## Run attempts

PBS `.o` and `.e` files in `outputs/` are the authoritative raw run records.

