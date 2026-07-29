# CCE13-CrayMPICH8 Build

Baseline LULESH build using the default Aspire2A Cray programming environment:

- compiler environment: `PrgEnv-cray/8.3.3`
- compiler module: `cce/13.0.2`
- MPI module: `cray-mpich/8.1.15`
- C++ compiler wrapper: `CC`
- MPI launcher: `mpirun` / `mpiexec` from `cray-pals/1.1.6`
- SILO: `Off`

Use `build_lulesh.pbs` to run the build through PBS. The PBS job calls
`build_lulesh.sh`, which follows the upstream LULESH CMake build path.
