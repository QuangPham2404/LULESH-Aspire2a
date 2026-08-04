# CCE13-CrayMPICH8-smoke-s10-newWF Run

## Summary

Repeat the one-rank LULESH `-s 10` smoke run using the new workflow and the
successful `CCE13-CrayMPICH8-newWF` Release build with SILO disabled.

## Run configuration

- experiment ID: `CCE13-CrayMPICH8-smoke-s10-newWF`
- build: `CCE13-CrayMPICH8-newWF`
- successful build binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0`
- compiler environment: `PrgEnv-cray/8.3.3`
- compiler: Cray `CC`, CCE 13.0.2
- MPI implementation: Cray MPICH 8.1.15
- input parameters: `-s 10`
- command: `mpirun -np 1 <successful-build-binary> -s 10`
- run resources: `select=1:ncpus=1:mpiprocs=1:mem=1gb`, walltime `00:10:00`
- PBS output directory: `outputs/`

## Run attempts

### CCE13-CrayMPICH8-smoke-s10-newWF_v1

- Status: success
- PBS job ID: `15086010.pbs101`
- Timestamp: `2026-08-04T09:33:38Z`
- Hostname/node: `x1002c4s7b0n0`
- PBS exit status: `0`
- PBS walltime: `00:00:06`
- stdout: `outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.o`
- stderr: `outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.e`
- Command: `mpirun -np 1 <successful-build-binary> -s 10`
- Observed error: none
- Normal application output: present
- Problem size: `10`
- MPI tasks: `1`
- Iteration count: `231`
- Final Origin Energy: `2.720531e+04`
- MaxAbsDiff: `2.273737e-12`
- TotalAbsDiff: `1.659646e-11`
- MaxRelDiff: `4.649603e-14`
- LULESH elapsed time: `0.35 s`
- FOM: `656.99887 z/s`
