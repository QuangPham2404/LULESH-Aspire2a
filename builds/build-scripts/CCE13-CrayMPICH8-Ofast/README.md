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

No build attempt has been submitted yet.

## BUILD error-patching record

No build errors recorded.
