# CCE13-CrayMPICH8-Ofast-s30 Run

Run the explicit CCE13 `-Ofast` build with `-s 30`, one MPI rank, and one
OpenMP thread. This result requires an additional scientific-accuracy review
because `-Ofast` may enable unsafe floating-point transformations.

- experiment ID: `CCE13-CrayMPICH8-Ofast-s30`
- build: `CCE13-CrayMPICH8-Ofast`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-Ofast/lulesh2.0`
- effective flags: `-fopenmp -Ofast -DNDEBUG`
- input: `-s 30`
- MPI ranks: `1`
- OpenMP threads: `1`

## Run attempts

### `CCE13-CrayMPICH8-Ofast-s30_v1`

- PBS job: `15096940.pbs101`
- PBS state/exit: `F / 0`
- node: `x1001c6s7b1n0`
- stdout: `outputs/CCE13-CrayMPICH8-Ofast-s30_v1.o`
- stderr: `outputs/CCE13-CrayMPICH8-Ofast-s30_v1.e`
- LULESH elapsed time: `17 s`
- FOM: `1484.2957 z/s`
- correctness: failed because `MaxRelDiff = -nan`
- scientific-correctness handling: result preserved; no patch attempted; the
  run is excluded from valid optimization selection pending investigation

## RUNTIME error-patching record

No runtime errors recorded.
