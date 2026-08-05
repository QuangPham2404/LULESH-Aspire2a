# LULESH Application Overview

## Source

- Project: Livermore Unstructured Lagrangian Explicit Shock Hydrodynamics
  (LULESH) 2.x
- Repository: https://github.com/LLNL/LULESH
- Source revision used in this workspace:
  `3e01c40b3281aadb7f996525cdd4a3354f6d3801`
- Local/Aspire2A source path: `builds/source/LULESH-newWF`

## What the application does

LULESH is an LLNL proxy application for an unstructured Lagrangian explicit
shock-hydrodynamics calculation. It solves a Sedov blast-wave problem on a
three-dimensional mesh and contains MPI and OpenMP parallel implementations.
The code is useful for exercising compiler, MPI, threading, memory-access, and
node-placement behavior in an HPC workflow.

This document describes the application and its normal build/run interface.
Optimization hypotheses, experiment priorities, comparisons, and conclusions
belong in `planning/`, not here.

## Build overview

The repository provides CMake and Makefile build systems. The workflow uses
CMake with the Cray `CC` C++ wrapper selected by the active programming
environment.

Required build components:

- CMake;
- a C++ compiler and C++ MPI wrapper;
- an MPI implementation and launcher;
- OpenMP support when `WITH_OPENMP=On`.

SILO is optional and is disabled for the baseline builds. It is only needed
when visualization output is required.

Example manual build from the source directory:

```bash
mkdir build-example
cd build-example
cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CXX_COMPILER="$(command -v CC)" \
  -DMPI_CXX_COMPILER="$(command -v CC)" \
  -DWITH_MPI=On \
  -DWITH_OPENMP=On \
  -DWITH_SILO=Off \
  ..
cmake --build . --parallel 8
```

The expected executable is `lulesh2.0` in the build directory.

## Run overview

The MPI launcher runs the executable. The simplest one-rank smoke command is:

```bash
mpirun -np 1 ./lulesh2.0 -s 10
```

Important command-line options include:

- `-s <integer>`: mesh size per domain;
- `-i <integer>`: fixed iteration count;
- `-b <integer>`: region-balance setting;
- `-c <integer>`: relative region-cost setting;
- `-p`: print progress;
- `-v`: write visualization output when SILO support is enabled;
- `-h`: show help.

The baseline workflow uses `-s 10`, one MPI task, and one OpenMP thread.

## Correctness and output markers

A completed run should contain:

- `Run completed:`;
- problem size, MPI task count, and iteration count;
- `Final Origin Energy`;
- `MaxAbsDiff`;
- `TotalAbsDiff`;
- `MaxRelDiff`;
- `Elapsed time`;
- `FOM`.

The correctness fields are the energy-array comparison reported by LULESH.
For a correctness-passing result, the difference fields must be finite and
within the acceptance criteria defined for the relevant experiment. A value
such as `NaN` or `-nan` is not a passing correctness result even if the process
exits successfully.

## Baseline command

After selecting a programming environment and building the executable, the
baseline command is:

```bash
export OMP_NUM_THREADS=1
mpirun -np 1 ./lulesh2.0 -s 10
```

The baseline record must preserve the compiler environment, source revision,
build flags, input arguments, raw output paths, timing, FOM, and correctness
fields. This overview does not interpret those measurements or recommend an
optimization direction.
