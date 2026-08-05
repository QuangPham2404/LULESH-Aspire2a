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

### AOCC-CrayMPICH8-smoke-s10_v1

- Status: success
- PBS job ID: `15090036.pbs101`
- PBS state: `F`
- PBS exit status: `0`
- Timestamp: `2026-08-05T00:05:46Z`
- Hostname/node: `x1001c3s2b1n0`
- PBS walltime: `00:00:14`
- stdout: `outputs/AOCC-CrayMPICH8-smoke-s10_v1.o`
- stderr: `outputs/AOCC-CrayMPICH8-smoke-s10_v1.e`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-AOCC-CrayMPICH8-Release/lulesh2.0`
- source commit: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- input parameters: `-s 10`
- MPI tasks: `1`
- OpenMP threads: `1`
- iterations: `231`
- final origin energy: `2.720531e+04`
- MaxAbsDiff: `2.273737e-12`
- TotalAbsDiff: `1.659646e-11`
- MaxRelDiff: `4.649603e-14`
- LULESH elapsed time: `0.26 s`
- FOM: `895.58097 z/s`
- correctness: passed; expected output and correctness fields were present.
- Observed error: none

PBS `.o` and `.e` files in `outputs/` are the authoritative raw run records.
