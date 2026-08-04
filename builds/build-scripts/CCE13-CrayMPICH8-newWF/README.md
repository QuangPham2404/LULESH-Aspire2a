# CCE13-CrayMPICH8-newWF Build

## Summary

Repeat the LULESH baseline build using the defined workflow and the default
Aspire2A Cray environment. SILO is disabled and the build type is Release.

## Build configuration

- source: `https://github.com/LLNL/LULESH.git`
- source path on Aspire2A: `builds/source/LULESH-newWF`
- source commit: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- compiler environment: `PrgEnv-cray/8.3.3`
- compiler: Cray `CC`, CCE 13.0.2
- MPI compiler: Cray `CC` with Cray MPICH 8.1.15
- build type: `Release`
- `WITH_MPI`: `On`
- `WITH_OPENMP`: `On`
- `WITH_SILO`: `Off`
- build resources: `select=1:ncpus=8:mem=4gb`, walltime `00:20:00`
- PBS output directory: `outputs/`

## Build attempts

### CCE13-CrayMPICH8-newWF_v1

- Status: success
- PBS job ID: `15086004.pbs101`
- Timestamp: `2026-08-04T09:32:29Z`
- Hostname/node: `x1001c6s1b0n0`
- PBS exit status: `0`
- PBS walltime: `00:00:13`
- stdout: `outputs/CCE13-CrayMPICH8-newWF_v1.o`
- stderr: `outputs/CCE13-CrayMPICH8-newWF_v1.e`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0`
- Observed error: none
- Result: Release build completed successfully with MPI and OpenMP enabled and SILO disabled.
