# `results/scripts/`

Scripts in this directory extract and transform values from raw experiment
output into files under `results/`. Each script should document its input
files, output files, expected schema, and application-specific assumptions.

The current LULESH extraction script accepts build and run PBS output paths,
appends a compatible LULESH run to `results/metrics.csv`, rejects duplicate
experiment attempts, and regenerates `results/RESULTS.md`. It assumes the
existing LULESH schema and validates the expected run metadata and correctness
fields before writing a row.

Example:

```text
python3 results/scripts/extract_lulesh_results.py \
  --build-name AOCC-CrayMPICH8 \
  --build-stdout builds/build-scripts/AOCC-CrayMPICH8/outputs/AOCC-CrayMPICH8_v1.2.o \
  --build-stderr builds/build-scripts/AOCC-CrayMPICH8/outputs/AOCC-CrayMPICH8_v1.2.e \
  --run-stdout experiments/AOCC-CrayMPICH8-smoke-s10/outputs/AOCC-CrayMPICH8-smoke-s10_v1.o \
  --run-stderr experiments/AOCC-CrayMPICH8-smoke-s10/outputs/AOCC-CrayMPICH8-smoke-s10_v1.e
```
