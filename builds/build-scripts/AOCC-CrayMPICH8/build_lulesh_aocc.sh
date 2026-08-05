#!/usr/bin/env bash
# Build LULESH from the repository root using the AOCC environment; inputs are
# the source tree and optional BUILD_JOBS/BUILD_TYPE overrides; output is the
# AOCC-specific build directory and the PBS-captured build metadata.
set -euo pipefail

REPO_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)
BUILD_NAME="AOCC-CrayMPICH8"
SOURCE_DIR="${SOURCE_DIR:-${REPO_ROOT}/builds/source/LULESH-newWF}"
BUILD_TYPE="${BUILD_TYPE:-Release}"
BUILD_DIR="${BUILD_DIR:-${SOURCE_DIR}/build-${BUILD_NAME}-${BUILD_TYPE}}"
INSTALL_PREFIX="${INSTALL_PREFIX:-${SOURCE_DIR}/install-${BUILD_NAME}-${BUILD_TYPE}}"

record() {
  printf '%s\n' "$*"
}

record_cmd() {
  record "\$ $*"
  "$@"
}

record "build_id: build-${BUILD_NAME}"
record "timestamp_utc: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
record "hostname: $(hostname)"
record "repo_root: ${REPO_ROOT}"
record "source_dir: ${SOURCE_DIR}"
record "build_dir: ${BUILD_DIR}"
record "install_prefix: ${INSTALL_PREFIX}"
record "source_commit: $(git -C "${SOURCE_DIR}" rev-parse HEAD 2>/dev/null || printf 'unknown')"
record "build_type: ${BUILD_TYPE}"
record "with_mpi: On"
record "with_openmp: On"
record "with_silo: Off"
record "requested_build_jobs: ${BUILD_JOBS:-8}"
record

for tool in cmake CC mpirun mpiexec git; do
  command -v "${tool}" >/dev/null 2>&1 || {
    record "ERROR: required tool not found: ${tool}" >&2
    exit 1
  }
done

[[ -f "${SOURCE_DIR}/CMakeLists.txt" ]] || {
  record "ERROR: LULESH source not found at ${SOURCE_DIR}" >&2
  exit 1
}

record '== loaded modules =='
module list 2>&1
record
record '== toolchain =='
for tool in CC cmake mpirun mpiexec; do
  record "${tool}: $(command -v "${tool}")"
done
record_cmd CC --version
record_cmd cmake --version
record_cmd mpirun --version
record

mkdir -p "${BUILD_DIR}"
cd "${BUILD_DIR}"

record '== cmake configure =='
record_cmd cmake \
  -DCMAKE_BUILD_TYPE="${BUILD_TYPE}" \
  -DCMAKE_CXX_COMPILER="$(command -v CC)" \
  -DMPI_CXX_COMPILER="$(command -v CC)" \
  -DWITH_MPI=On \
  -DWITH_OPENMP=On \
  -DWITH_SILO=Off \
  -DCMAKE_INSTALL_PREFIX="${INSTALL_PREFIX}" \
  "${SOURCE_DIR}"

record '== cmake build =='
record_cmd cmake --build . --parallel "${BUILD_JOBS:-8}"

if [[ -x "${BUILD_DIR}/lulesh2.0" ]]; then
  record 'build_result: success'
  record "binary: ${BUILD_DIR}/lulesh2.0"
else
  record 'build_result: failed'
  record "ERROR: expected binary not found at ${BUILD_DIR}/lulesh2.0" >&2
  exit 1
fi

