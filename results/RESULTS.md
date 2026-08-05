# LULESH Results

## Run Records

| Experiment | Build | Attempt | PBS job | Input | Elapsed (s) | FOM (z/s) | Correctness | Status |
| --- | --- | --- | --- | --- | ---: | ---: | --- | --- |
| CCE13-CrayMPICH8-smoke-s10-newWF | CCE13-CrayMPICH8-newWF | CCE13-CrayMPICH8-smoke-s10-newWF_v1 | 15086010.pbs101 | `-s 10` | 0.35 | 656.99887 | passed | success |
| AOCC-CrayMPICH8-smoke-s10 | AOCC-CrayMPICH8 | AOCC-CrayMPICH8-smoke-s10_v1 | 15090036.pbs101 | `-s 10` | 0.26 | 895.58097 | passed | success |

## Provenance

### CCE13-CrayMPICH8-smoke-s10-newWF / CCE13-CrayMPICH8-smoke-s10-newWF_v1

- `timestamp_utc`: `2026-08-04T09:33:38Z`
- `hostname`: `x1002c4s7b0n0`
- `source_commit`: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- `compiler`: `Cray CC`
- `compiler_version`: `13.0.2`
- `mpi_implementation`: `Cray MPICH`
- `mpi_version`: `8.1.15`
- `mpi_launcher_version`: `1.1.6`
- `loaded_modules`: `craype-x86-rome;craype/2.7.15;libfabric/1.11.0.4.125;cray-dsmml/0.2.2;craype-network-ofi;cray-mpich/8.1.15;perftools-base/22.04.0;cray-pals/1.1.6;cce/13.0.2;PrgEnv-cray/8.3.3`
- `build_flags`: `Release;WITH_MPI=On;WITH_OPENMP=On;WITH_SILO=Off`
- `binary_path`: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0`
- `stdout_path`: `experiments/CCE13-CrayMPICH8-smoke-s10-newWF/outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.o`
- `stderr_path`: `experiments/CCE13-CrayMPICH8-smoke-s10-newWF/outputs/CCE13-CrayMPICH8-smoke-s10-newWF_v1.e`
- `build_stdout_path`: `builds/build-scripts/CCE13-CrayMPICH8-newWF/outputs/CCE13-CrayMPICH8-newWF_v1.o`
- `build_stderr_path`: `builds/build-scripts/CCE13-CrayMPICH8-newWF/outputs/CCE13-CrayMPICH8-newWF_v1.e`
### AOCC-CrayMPICH8-smoke-s10 / AOCC-CrayMPICH8-smoke-s10_v1

- `timestamp_utc`: `2026-08-05T00:05:46Z`
- `hostname`: `x1001c3s2b1n0`
- `source_commit`: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- `compiler`: `AOCC CC`
- `compiler_version`: `3.2.0`
- `mpi_implementation`: `Cray MPICH`
- `mpi_version`: `8.1.15`
- `mpi_launcher_version`: `1.1.6`
- `loaded_modules`: `craype-x86-rome;craype/2.7.15;libfabric/1.11.0.4.125;cray-dsmml/0.2.2;craype-network-ofi;cray-mpich/8.1.15;perftools-base/22.04.0;cray-pals/1.1.6;aocc/3.2.0;PrgEnv-aocc/8.3.3`
- `build_flags`: `Release;WITH_MPI=On;WITH_OPENMP=On;WITH_SILO=Off`
- `binary_path`: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-AOCC-CrayMPICH8-Release/lulesh2.0`
- `stdout_path`: `experiments/AOCC-CrayMPICH8-smoke-s10/outputs/AOCC-CrayMPICH8-smoke-s10_v1.o`
- `stderr_path`: `experiments/AOCC-CrayMPICH8-smoke-s10/outputs/AOCC-CrayMPICH8-smoke-s10_v1.e`
- `build_stdout_path`: `builds/build-scripts/AOCC-CrayMPICH8/outputs/AOCC-CrayMPICH8_v1.2.o`
- `build_stderr_path`: `builds/build-scripts/AOCC-CrayMPICH8/outputs/AOCC-CrayMPICH8_v1.2.e`

No optimization analysis is included. Analysis belongs in a later planning session.
