# AOCC-CrayMPICH8 Build

## Summary

Build LULESH with the default Aspire2A AOCC programming environment, Cray
MPICH, MPI, and OpenMP enabled, and SILO disabled.

## Build configuration

- source path on Aspire2A: `builds/source/LULESH-newWF`
- source commit: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- compiler environment: `PrgEnv-aocc/8.3.3`
- compiler: AOCC through Cray `CC`
- MPI compiler: Cray `CC` with Cray MPICH 8.1.15
- build type: `Release`
- `WITH_MPI`: `On`
- `WITH_OPENMP`: `On`
- `WITH_SILO`: `Off`
- build resources: `select=1:ncpus=8:mem=4gb`, walltime `00:20:00`
- PBS output directory: `outputs/`

## Build attempts

Results will be recorded here after submission. PBS `.o` and `.e` files in
`outputs/` are the authoritative raw build records.

