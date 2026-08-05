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

### AOCC-CrayMPICH8_v1

- Status: failed before the build script started
- PBS job ID: `15090029.pbs101`
- PBS state: `E`
- PBS exit status: `127`
- Node allocation: `x1001c7s6b1n0`
- Requested resources: `select=1:ncpus=8:mem=4gb`, walltime `00:20:00`
- Observed error: PBS resolved the relative output path against the repository
  root and could not stage the requested output files because the root-level
  `outputs/` directory did not exist. No build `.o` or `.e` file was produced.
- Suspected cause: the job was submitted from the repository root instead of
  the build-script directory.
- Patch/workflow change: submit from
  `builds/build-scripts/AOCC-CrayMPICH8/` and use new attempt-specific output
  names.
- Next attempt: `AOCC-CrayMPICH8_v1.1`.

### AOCC-CrayMPICH8_v1.1

- Status: failed during preflight
- PBS job ID: `15090033.pbs101`
- PBS state: `F`
- PBS exit status: `1`
- Timestamp: `2026-08-05T00:03:30Z`
- Hostname/node: `x1001c7s6b1n0`
- PBS walltime: `00:00:02`
- stdout: `outputs/AOCC-CrayMPICH8_v1.1.o`
- stderr: `outputs/AOCC-CrayMPICH8_v1.1.e`
- Observed error: `git` was not available in the compute-node job PATH.
- Suspected cause: the build preflight required Git even though Git is not
  needed by the compiler or build commands.
- Patch/workflow change: remove Git from the compute-node tool requirement and
  pass the verified source commit as explicit PBS metadata.
- Next attempt: `AOCC-CrayMPICH8_v1.2`.

### AOCC-CrayMPICH8_v1.2

- Status: success
- PBS job ID: `15090035.pbs101`
- PBS state: `E`
- PBS exit status: `0`
- Timestamp: `2026-08-05T00:05:07Z`
- Hostname/node: `x1001c7s6b1n0`
- PBS walltime: `00:00:21`
- stdout: `outputs/AOCC-CrayMPICH8_v1.2.o`
- stderr: `outputs/AOCC-CrayMPICH8_v1.2.e`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-AOCC-CrayMPICH8-Release/lulesh2.0`
- source commit: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- compiler environment: `PrgEnv-aocc/8.3.3`, AOCC 3.2.0, Cray MPICH 8.1.15
- build flags: `Release; WITH_MPI=On; WITH_OPENMP=On; WITH_SILO=Off`
- Observed error: none
- Result: executable produced and build output completed successfully.

PBS `.o` and `.e` files in `outputs/` are the authoritative raw build records.
