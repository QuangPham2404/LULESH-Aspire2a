#!/usr/bin/env bash
# Shared run helper for the controlled CCE13 OpenMP affinity repeatability
# experiment (TASK-001); the expected working directory is the PBS submission
# directory (this experiment directory). The PBS wrappers supply OMP_THREADS,
# EXPERIMENT_ID, ATTEMPT_SUFFIX, and REQUESTED_RESOURCES. This helper emits
# the metadata required by results/scripts/extract_lulesh_results.py, exports
# the controlled affinity environment (identical across configurations except
# the thread count), and runs only `mpirun -np 1 <binary> -s 30`. Affinity
# warnings are never suppressed; stderr is preserved as PBS evidence.

set -euo pipefail
cd "${PBS_O_WORKDIR}"
REPO_ROOT="/home/users/ntu/pham0094/scratch/LULESH-Aspire2a"
BINARY="${REPO_ROOT}/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0"
OMP_THREADS="${OMP_THREADS:?OMP_THREADS is required}"
EXPERIMENT_ID="${EXPERIMENT_ID:?EXPERIMENT_ID is required}"
ATTEMPT_SUFFIX="${ATTEMPT_SUFFIX:?ATTEMPT_SUFFIX is required}"
ATTEMPT="${EXPERIMENT_ID}_${ATTEMPT_SUFFIX}"
REQUESTED_RESOURCES="${REQUESTED_RESOURCES:?REQUESTED_RESOURCES is required}"
SOURCE_COMMIT="3e01c40b3281aadb7f996525cdd4a3354f6d3801"

# Controlled affinity environment; identical across configurations except
# OMP_NUM_THREADS, whose value each wrapper supplies.
export OMP_NUM_THREADS="${OMP_THREADS}"
export OMP_PLACES=cores
export OMP_PROC_BIND=spread
export OMP_DISPLAY_AFFINITY=TRUE

echo "experiment_id: ${EXPERIMENT_ID}"
echo "attempt: ${ATTEMPT}"
echo "pbs_job_id: ${PBS_JOBID:-unknown}"
echo "timestamp_utc: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "hostname: $(hostname)"
echo "binary: ${BINARY}"
echo "source_commit: ${SOURCE_COMMIT}"
echo "input_parameters: -s 30"
echo "mpi_tasks: 1"
echo "openmp_threads: ${OMP_NUM_THREADS}"
echo "omp_places: ${OMP_PLACES}"
echo "omp_proc_bind: ${OMP_PROC_BIND}"
echo "omp_display_affinity: ${OMP_DISPLAY_AFFINITY}"
echo "requested_resources: ${REQUESTED_RESOURCES}"
echo
command -v mpirun >/dev/null 2>&1 || { echo "ERROR: mpirun missing" >&2; exit 1; }
[[ -x "${BINARY}" ]] || { echo "ERROR: binary missing: ${BINARY}" >&2; exit 1; }
echo '== loaded modules =='
module list 2>&1
echo '== toolchain =='
CC --version 2>/dev/null || true
mpirun --version
echo "omp_num_threads: ${OMP_NUM_THREADS}"
echo "omp_places: ${OMP_PLACES}"
echo "omp_proc_bind: ${OMP_PROC_BIND}"
echo "omp_display_affinity: ${OMP_DISPLAY_AFFINITY}"
echo '== run =='
mpirun -np 1 "${BINARY}" -s 30
