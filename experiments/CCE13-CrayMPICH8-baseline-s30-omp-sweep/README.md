# CCE13-CrayMPICH8-baseline-s30-omp-sweep

Scale OpenMP threads using the existing CCE13 Release (`-O3 -DNDEBUG`) binary
with one MPI rank and `-s 30`. The one-thread baseline is already recorded in
the MPI-rank-1 result, so this sweep adds 8, 16, and 32 threads. No rebuild is
required.

| Experiment | MPI ranks | OpenMP threads | Resources |
| --- | ---: | ---: | --- |
| `CCE13-CrayMPICH8-baseline-s30-omp8` | 1 | 8 | `select=1:ncpus=8:mpiprocs=1:mem=16gb` |
| `CCE13-CrayMPICH8-baseline-s30-omp16` | 1 | 16 | `select=1:ncpus=16:mpiprocs=1:mem=16gb` |
| `CCE13-CrayMPICH8-baseline-s30-omp32` | 1 | 32 | `select=1:ncpus=32:mpiprocs=1:mem=16gb` |

- binary: `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0`
- effective flags: `-fopenmp -O3 -DNDEBUG`
- source revision: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`

## Run attempts

All three runs completed with PBS state `F / 0` and finite correctness:

- `CCE13-CrayMPICH8-baseline-s30-omp8_v1`, PBS job `15097075.pbs101`, node
  `x1002c5s2b0n0`, elapsed `6.6 s`, FOM `3784.5446`, `MaxRelDiff = 1.461140e-12`;
- `CCE13-CrayMPICH8-baseline-s30-omp16_v1`, PBS job `15097076.pbs101`, node
  `x1001c4s4b0n1`, elapsed `17 s`, FOM `1470.1691`,
  `MaxRelDiff = 1.461140e-12`;
- `CCE13-CrayMPICH8-baseline-s30-omp32_v1`, PBS job `15097077.pbs101`, node
  `x1001c2s1b0n1`, elapsed `31 s`, FOM `806.53914`,
  `MaxRelDiff = 1.461140e-12`.

Each stderr file contains the Cray OpenMP warning that requested thread count
or affinity may oversubscribe available CPU resources. The warning was
preserved as provenance; no affinity or resource-policy patch was attempted.

## RUNTIME error-patching record

No runtime errors recorded.
