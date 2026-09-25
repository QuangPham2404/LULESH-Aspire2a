# `experiments/`

This directory contains run-specific experiment folders.

Each subdirectory should represent a specific optimization run or run family.
Examples:

```text
experiments/
├── ICC25-O3/
└── ICC25-O2/
```

Suggested contents for each experiment directory:

```text
experiments/<run_name>/
├── README.md
├── run_<name>.pbs
└── outputs/
    ├── <name>_v1.o
    └── <name>_v1.e
```

The experiment `README.md` should be concise and include the run purpose,
metadata, command/script summary, expected output, and validation notes.

Keep raw PBS output files in the experiment's `outputs/` directory. Give every
retry a new attempt-specific output name so prior evidence is preserved.
Extracted result files belong in `results/`.
