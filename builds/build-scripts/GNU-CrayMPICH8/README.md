# GNU-CrayMPICH8 Build

## Summary

Build LULESH with the default Aspire2A GNU programming environment, Cray
MPICH, MPI, and OpenMP enabled, and SILO disabled.

## Build configuration

- source path: `builds/source/LULESH-newWF`
- source commit: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- compiler environment: `PrgEnv-gnu/8.3.3`
- compiler: GNU through Cray `CC`
- MPI compiler: Cray `CC` with Cray MPICH 8.1.15
- build type: `Release`
- `WITH_MPI`: `On`
- `WITH_OPENMP`: `On`
- `WITH_SILO`: `Off`
- build resources: `select=1:ncpus=8:mem=4gb`, walltime `00:20:00`
- PBS output directory: `outputs/`

## Build attempts

### GNU-CrayMPICH8_v1

- Status: success
- PBS job ID: `15090186.pbs101`
- PBS state: `F`
- PBS exit status: `0`
- Timestamp: `2026-08-05T00:54:02Z`
- Hostname/node: `x1003c7s2b0n0`
- PBS walltime: `00:00:06`
- stdout: `outputs/GNU-CrayMPICH8_v1.o`
- stderr: `outputs/GNU-CrayMPICH8_v1.e`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-GNU-CrayMPICH8-Release/lulesh2.0`
- compiler: GNU through Cray `CC`
- Result: executable produced successfully.

PBS `.o` and `.e` files in `outputs/` are the authoritative raw build records.
