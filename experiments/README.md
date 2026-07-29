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
├── run.pbs
├── <job_name>.o<PBS_JOB_ID>
└── <job_name>.e<PBS_JOB_ID>
```

The experiment `README.md` should be concise and include the run purpose,
metadata, command/script summary, expected output, and validation notes.

Raw PBS output files stay here. Extracted result files belong in `results/`.
