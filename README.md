# LULESH Aspire2A Optimization Workspace

Application GitHub link: https://github.com/LLNL/LULESH

This repository is a flexible blueprint for Codex-assisted HPC optimization
work. The exact files can change by application, but the workflow should stay
consistent:

1. Discuss optimization ideas and choose experiments to test.
2. Prepare build scripts, run scripts, and result extraction scripts.
3. Review non-routine scripts before submission.
4. Submit compute work through PBS on Aspire2A.
5. Record errors, metadata, raw output, and validation details.
6. Extract result files from raw experiment output.
7. Write planning and analysis together, then choose the next experiment.

The local PC and Aspire2A should both use real Git clones of this repository.
The Aspire2A clone is the working copy for remote builds and batch execution,
while Git provides the shared project state for scripts, plans, extracted
results, progress notes, and analysis.

Prefer local Git operations for commits and pushes. Aspire2A should not store
GitHub credentials, and Codex should not push from Aspire2A unless explicitly
approved.

## Directory Roles

### `builds/`

Build-related material.

Expected subdirectories:

```text
builds/
├── source/
├── build-scripts/
└── extra-packages/
```

- `source/`: source code cloned or copied for building the application with
  different compilation methods.
- `build-scripts/`: reusable build scripts kept for record and handoff.
- `extra-packages/`: any approved extra packages needed to support builds.

### `experiments/`

Run-specific experiment directories.

Each subdirectory should represent one optimization run or run family, for
example:

```text
experiments/
├── ICC25-O3/
└── ICC25-O2/
```

Each experiment directory should contain the run script, a concise `README.md`
with metadata and purpose, and raw PBS output files such as `.o` and `.e`.

### `planning/`

Planning and result analysis.

Keep experiment plans and analysis together here to avoid splitting the story
across multiple directories. A `PLANS.md` file can describe the hypothesis,
execution plan, completed results, interpretation, and next steps.

### `results/`

Extracted result files from raw output under `experiments/`.

Directory-specific extraction or plotting scripts should live under
`results/scripts/`.

### `progress/`

Session progress notes and technical diary entries.

Use date-based files such as:

```text
progress/2026-07-29-progress.md
```

These files should capture what happened in each work session, including
decisions, blockers, fixes, and handoff context.

### `scripts/`

General reusable scripts that do not naturally belong to another directory.

Examples include sync helpers, repository checks, remote inspection helpers, or
workflow utilities. Scripts specific to builds, experiments, or result
extraction should stay inside the corresponding directory.

With the two-clone workflow, these scripts should prefer Git-aware operations
and checks over copying the full project tree manually.

## Run Metadata

Each run should record enough information to reproduce and audit the result:

- experiment ID
- PBS job ID
- timestamp
- hostname or node allocation
- compiler and compiler version
- MPI implementation and version
- loaded modules
- build flags
- input parameters
- requested resources
- runtime
- correctness or convergence result
- stdout path
- stderr path
- exit status

Do not classify a run as successful from exit code alone. Validate the expected
LULESH output and correctness criteria.

## Aspire2A Remote Path

The remote project root is:

```text
/home/users/ntu/pham0094/scratch/LULESH-Aspire2a
```

All Codex-controlled remote work should stay inside that path unless explicitly
approved otherwise.

This path should be a Git clone of the repository, not an untracked copy.
Generated build trees, installed extra packages, and compiled artifacts are kept
out of Git by `.gitignore`.
