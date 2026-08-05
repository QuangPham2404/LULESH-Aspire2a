# CCE13-CrayMPICH8-Ofast Build

This build tests explicit `-Ofast` optimization with the CCE13 environment.
It uses the LULESH source already cloned on Aspire2A, enables MPI and OpenMP,
disables SILO, and writes the PBS build record to `outputs/`.

- build name: `CCE13-CrayMPICH8-Ofast`
- build type: `Release`
- effective Release flags: `-Ofast -DNDEBUG`
- compiler: Cray `CC`
- MPI compiler: Cray `CC` through `MPI_CXX_COMPILER`
- source: `builds/source/LULESH-newWF`
- binary: `builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-Ofast/lulesh2.0`

## Build attempts

### `CCE13-CrayMPICH8-Ofast_v1`

- PBS job: `15096923.pbs101`
- PBS state/exit: `F / 127`
- intended stdout: `outputs/CCE13-CrayMPICH8-Ofast_v1.o`
- intended stderr: `outputs/CCE13-CrayMPICH8-Ofast_v1.e`
- observed error: the expected build output files were not created
- suspected cause: PBS resolved the relative `#PBS -o/-e` paths against the
  qsub submission directory because the job was submitted from the repository
  root rather than this build directory
- patch: submit the retry from this build-script directory; preserve the
  attempt-specific filenames
- retry: `CCE13-CrayMPICH8-Ofast_v1.1`

### `CCE13-CrayMPICH8-Ofast_v1.1`

- PBS job: `15096936.pbs101`
- PBS state/exit: `F / 0`
- node: `x1002c6s3b0n0`
- stdout: `outputs/CCE13-CrayMPICH8-Ofast_v1.1.o`
- stderr: `outputs/CCE13-CrayMPICH8-Ofast_v1.1.e`
- result: build completed successfully; generated flags were
  `-fopenmp -Ofast -DNDEBUG`

## BUILD error-patching record

No build errors recorded.
