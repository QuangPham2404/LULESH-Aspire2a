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

- Status: pending
- PBS job ID: pending
- stdout: `outputs/CCE13-CrayMPICH8-newWF_v1.o`
- stderr: `outputs/CCE13-CrayMPICH8-newWF_v1.e`
- Observed error: none yet
- Patch or workflow change: first execution of the defined workflow
