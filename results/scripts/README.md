# `results/scripts/`

Scripts in this directory extract and transform values from raw experiment
output into files under `results/`. Each script should document its input
files, output files, expected schema, and application-specific assumptions.

The current LULESH extraction script processes only the new-workflow baseline
run and intentionally excludes the older smoke run.
