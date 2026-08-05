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

### GNU-CrayMPICH8-smoke-s10_v1

- Status: success
- PBS job ID: `15090190.pbs101`
- PBS state: `F`
- PBS exit status: `0`
- Timestamp: `2026-08-05T00:54:34Z`
- Hostname/node: `x1001c6s0b0n1`
- PBS walltime: `00:00:03`
- stdout: `outputs/GNU-CrayMPICH8-smoke-s10_v1.o`
- stderr: `outputs/GNU-CrayMPICH8-smoke-s10_v1.e`
- input parameters: `-s 10`
- MPI tasks: `1`
- OpenMP threads: `1`
- iterations: `231`
- final origin energy: `2.720531e+04`
- MaxAbsDiff: `3.637979e-12`
- TotalAbsDiff: `1.809061e-11`
- MaxRelDiff: `3.938811e-14`
- LULESH elapsed time: `0.34 s`
- FOM: `682.15817 z/s`
- Correctness: passed.

PBS `.o` and `.e` files in `outputs/` are the authoritative raw run records.
