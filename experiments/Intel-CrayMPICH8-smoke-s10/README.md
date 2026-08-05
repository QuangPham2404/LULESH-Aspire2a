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

### Intel-CrayMPICH8-smoke-s10_v1

- Status: completed with correctness failure
- PBS job ID: `15090189.pbs101`
- PBS state: `F`
- PBS exit status: `0`
- Timestamp: `2026-08-05T00:54:34Z`
- Hostname/node: `x1001c6s0b0n1`
- PBS walltime: `00:00:09`
- stdout: `outputs/Intel-CrayMPICH8-smoke-s10_v1.o`
- stderr: `outputs/Intel-CrayMPICH8-smoke-s10_v1.e`
- input parameters: `-s 10`
- MPI tasks: `1`
- OpenMP threads: `1`
- iterations: `231`
- final origin energy: `2.720531e+04`
- MaxAbsDiff: `4.547474e-12`
- TotalAbsDiff: `2.695046e-11`
- MaxRelDiff: `-nan`
- LULESH elapsed time: `0.2 s`
- FOM: `1182.5021 z/s`
- Observed issue: application completed, but the non-finite `MaxRelDiff`
  fails the correctness check.

PBS `.o` and `.e` files in `outputs/` are the authoritative raw run records.
