#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT=$(cd "${SCRIPT_DIR}/../../.." && pwd)

BUILD_CATEGORY="CCE13-CrayMPICH8"
LULESH_REPO_URL="${LULESH_REPO_URL:-https://github.com/LLNL/LULESH.git}"
LULESH_REF="${LULESH_REF:-master}"
BUILD_TYPE="${BUILD_TYPE:-Release}"
WITH_MPI="${WITH_MPI:-On}"
WITH_OPENMP="${WITH_OPENMP:-On}"
WITH_SILO="${WITH_SILO:-Off}"

SOURCE_DIR="${SOURCE_DIR:-${REPO_ROOT}/builds/source/LULESH}"
BUILD_DIR="${BUILD_DIR:-${SOURCE_DIR}/build-${BUILD_CATEGORY}-${BUILD_TYPE}}"
INSTALL_PREFIX="${INSTALL_PREFIX:-${SOURCE_DIR}/install-${BUILD_CATEGORY}-${BUILD_TYPE}}"
RECORD_DIR="${RECORD_DIR:-${SCRIPT_DIR}/records}"
TIMESTAMP=$(date -u +"%Y%m%dT%H%M%SZ")
RECORD_FILE="${RECORD_DIR}/build-${BUILD_CATEGORY}-${TIMESTAMP}.txt"

mkdir -p "${RECORD_DIR}"
mkdir -p "$(dirname "${SOURCE_DIR}")"

record() {
  printf "%s\n" "$*" | tee -a "${RECORD_FILE}"
}

record_cmd() {
  record "\$ $*"
  "$@" 2>&1 | tee -a "${RECORD_FILE}"
}

record "experiment_id: build-${BUILD_CATEGORY}-${TIMESTAMP}"
record "timestamp_utc: ${TIMESTAMP}"
record "hostname: $(hostname)"
record "repo_root: ${REPO_ROOT}"
record "source_dir: ${SOURCE_DIR}"
record "build_dir: ${BUILD_DIR}"
record "install_prefix: ${INSTALL_PREFIX}"
record "lulesh_repo_url: ${LULESH_REPO_URL}"
record "lulesh_ref: ${LULESH_REF}"
record "build_type: ${BUILD_TYPE}"
record "with_mpi: ${WITH_MPI}"
record "with_openmp: ${WITH_OPENMP}"
record "with_silo: ${WITH_SILO}"
record ""

record "== loaded modules =="
module list 2>&1 | tee -a "${RECORD_FILE}"
record ""

record "== toolchain =="
for tool in git cmake make CC cc ftn mpirun mpiexec; do
  if command -v "${tool}" >/dev/null 2>&1; then
    record "${tool}: $(command -v "${tool}")"
  else
    record "${tool}: not found"
  fi
done
record ""

if ! command -v git >/dev/null 2>&1; then
  record "ERROR: git is not available on PATH."
  exit 1
fi

if ! command -v cmake >/dev/null 2>&1; then
  record "ERROR: cmake is not available on PATH."
  exit 1
fi

if ! command -v CC >/dev/null 2>&1; then
  record "ERROR: Cray C++ wrapper CC is not available on PATH."
  exit 1
fi

record_cmd cmake --version
record_cmd CC --version
record_cmd CC --cray-print-opts=all
record ""

if [[ ! -d "${SOURCE_DIR}/.git" ]]; then
  record "== cloning LULESH source =="
  record_cmd git clone "${LULESH_REPO_URL}" "${SOURCE_DIR}"
else
  record "== existing LULESH source detected =="
  record "No source update performed by default. Set UPDATE_SOURCE=1 to fetch and fast-forward."
fi

cd "${SOURCE_DIR}"

if [[ "${UPDATE_SOURCE:-0}" == "1" ]]; then
  record "== updating LULESH source =="
  record_cmd git fetch origin
  record_cmd git checkout "${LULESH_REF}"
  record_cmd git pull --ff-only
else
  record_cmd git checkout "${LULESH_REF}"
fi

LULESH_COMMIT=$(git rev-parse HEAD)
record "lulesh_commit: ${LULESH_COMMIT}"
record ""

mkdir -p "${BUILD_DIR}"
cd "${BUILD_DIR}"

record "== cmake configure =="
record_cmd cmake \
  -DCMAKE_BUILD_TYPE="${BUILD_TYPE}" \
  -DCMAKE_CXX_COMPILER="$(command -v CC)" \
  -DMPI_CXX_COMPILER="$(command -v CC)" \
  -DWITH_MPI="${WITH_MPI}" \
  -DWITH_OPENMP="${WITH_OPENMP}" \
  -DWITH_SILO="${WITH_SILO}" \
  -DCMAKE_INSTALL_PREFIX="${INSTALL_PREFIX}" \
  "${SOURCE_DIR}"

record ""
record "== cmake build =="
record_cmd cmake --build . --parallel "${BUILD_JOBS:-4}"

record ""
if [[ -x "${BUILD_DIR}/lulesh2.0" ]]; then
  record "build_result: success"
  record "binary: ${BUILD_DIR}/lulesh2.0"
else
  record "build_result: failed"
  record "ERROR: expected binary not found at ${BUILD_DIR}/lulesh2.0"
  exit 1
fi
