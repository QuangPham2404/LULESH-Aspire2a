# AOCC-CrayMPICH8-smoke-s10 Run

## Summary

Run the one-rank LULESH `-s 10` smoke test with the successful
`AOCC-CrayMPICH8` Release build and the default AOCC programming environment.

## Run configuration

- experiment ID: `AOCC-CrayMPICH8-smoke-s10`
- build: `AOCC-CrayMPICH8`
- input parameters: `-s 10`
- MPI tasks: `1`
- OpenMP threads: `1`
- command: `mpirun -np 1 <successful-build-binary> -s 10`
- compiler environment: `PrgEnv-aocc/8.3.3`
- run resources: `select=1:ncpus=1:mpiprocs=1:mem=1gb`, walltime `00:10:00`
- PBS output directory: `outputs/`

## Run attempts

Results will be recorded here after submission. PBS `.o` and `.e` files in
`outputs/` are the authoritative raw run records.

