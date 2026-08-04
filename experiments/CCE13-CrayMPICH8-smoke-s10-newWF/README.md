# CCE13-CrayMPICH8-smoke-s10-newWF Run

## Summary

Repeat the one-rank LULESH `-s 10` smoke run using the new workflow and the
successful `CCE13-CrayMPICH8-newWF` Release build with SILO disabled.

## Run configuration

- experiment ID: `CCE13-CrayMPICH8-smoke-s10-newWF`
- build: `CCE13-CrayMPICH8-newWF`
- compiler environment: `PrgEnv-cray/8.3.3`
- compiler: Cray `CC`, CCE 13.0.2
- MPI implementation: Cray MPICH 8.1.15
- input parameters: `-s 10`
- command: `mpirun -np 1 <successful-build-binary> -s 10`
- run resources: `select=1:ncpus=1:mpiprocs=1:mem=1gb`, walltime `00:10:00`
- PBS output directory: `outputs/`

## Run attempts

### CCE13-CrayMPICH8-smoke-s10-newWF_v1

- Status: pending build completion
- PBS job ID: pending
- stdout: `outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.o`
- stderr: `outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.e`
- Observed error: none yet
- Patch or workflow change: first execution of the defined workflow
