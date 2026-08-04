#!/usr/bin/env bash
set -euo pipefail

export PATH="${PATH:-}:/usr/local/bin:/usr/bin:/bin"

REPO_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)
BUILD_NAME="CCE13-CrayMPICH8-newWF"
SOURCE_DIR="${SOURCE_DIR:-${REPO_ROOT}/builds/source/LULESH-newWF}"
BUILD_TYPE="${BUILD_TYPE:-Release}"
BUILD_DIR="${BUILD_DIR:-${SOURCE_DIR}/build-${BUILD_NAME}-${BUILD_TYPE}}"
INSTALL_PREFIX="${INSTALL_PREFIX:-${SOURCE_DIR}/install-${BUILD_NAME}-${BUILD_TYPE}}"
RECORD_DIR="${RECORD_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/records}"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")
RECORD_FILE="${RECORD_DIR}/build-${BUILD_NAME}-${TIMESTAMP}.txt"

mkdir -p "${RECORD_DIR}" "${BUILD_DIR}"

record() {
  printf '%s\n' "$*" | tee -a "${RECORD_FILE}"
}

record_cmd() {
  record "\$ $*"
  "$@" 2>&1 | tee -a "${RECORD_FILE}"
}

record "experiment_id: build-${BUILD_NAME}-${TIMESTAMP}"
record "timestamp_utc: ${TIMESTAMP}"
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
record ""

record '== loaded modules =='
module list 2>&1 | tee -a "${RECORD_FILE}"
record ''

record '== toolchain =='
for tool in cmake make CC mpirun mpiexec; do
  if command -v "${tool}" >/dev/null 2>&1; then
    record "${tool}: $(command -v "${tool}")"
  else
    record "${tool}: not found"
  fi
done
record_cmd cmake --version
record_cmd CC --version
record_cmd mpirun --version
record ''

if [[ ! -f "${SOURCE_DIR}/CMakeLists.txt" ]]; then
  record "ERROR: LULESH source not found at ${SOURCE_DIR}."
  exit 1
fi

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
  record "ERROR: expected binary not found at ${BUILD_DIR}/lulesh2.0"
  exit 1
fi
