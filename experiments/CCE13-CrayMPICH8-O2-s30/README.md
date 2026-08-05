# CCE13-CrayMPICH8-O2-s30 Run

Run the explicit CCE13 `-O2` build with `-s 30`, one MPI rank, and one
OpenMP thread. Correctness is compared with the CCE13 Release baseline.

- experiment ID: `CCE13-CrayMPICH8-O2-s30`
- build: `CCE13-CrayMPICH8-O2`
- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-O2/lulesh2.0`
- effective flags: `-fopenmp -O2 -DNDEBUG`
- input: `-s 30`
- MPI ranks: `1`
- OpenMP threads: `1`

## Run attempts

### `CCE13-CrayMPICH8-O2-s30_v1`

- PBS job: `15096939.pbs101`
- PBS state/exit: `F / 0`
- node: `x1001c6s0b1n1`
- stdout: `outputs/CCE13-CrayMPICH8-O2-s30_v1.o`
- stderr: `outputs/CCE13-CrayMPICH8-O2-s30_v1.e`
- LULESH elapsed time: `22 s`
- FOM: `1167.0982 z/s`
- correctness: passed; `MaxRelDiff = 1.482369e-12`

## RUNTIME error-patching record

No runtime errors recorded.
