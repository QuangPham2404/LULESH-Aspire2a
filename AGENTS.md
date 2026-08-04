# Aspire2A Operating Rules

## Authentication

- Never request, read, store, transmit, echo, or log any SSH password.
- Never use `sshpass`, Expect, password files, clipboard extraction,
  environment variables, or command-line password arguments.
- Never attempt to modify SSH authentication settings.
- Never automate password entry.
- Never install tools merely to bypass interactive authentication.

## Persistent SSH connection

- Before remote work, check the connection with:

  `ssh -O check aspire2a`

- If the connection is unavailable, stop and ask the user to run:

  `aspire-connect`

- Do not initiate a normal interactive SSH login.

## Required SSH mode

- For every Codex-controlled SSH command, use:

  `ssh -o BatchMode=yes aspire2a '<command>'`

- For every Codex-controlled SCP command, use:

  `scp -o BatchMode=yes ...`

- For every Codex-controlled rsync command, use:

  `rsync -e 'ssh -o BatchMode=yes' ...`

## Remote scope

- Remote project root:

  `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a`

- Do not read, write, modify, or delete files outside the project root
  without explicit approval.
- Do not use `sudo`.
- Do not install Codex, package managers, background services, daemons,
  proxies, or remote agents on Aspire2A.
- Do not modify shared software. Most of the required package for buildings should be found from the available modules. If the agent need to install a new software package that is not available, you need to ask for the user permission first.
- During the execution process, you are only to create folders and create/edit files. Do NOT delete folders without asking for user permission.

## Scheduler policy

- Run computation through batch jobs via PBS.
- Do not perform computational workloads on login nodes.
- Do not poll PBS excessively.

## Result integrity

Each run should record:

- experiment ID;
- PBS job ID;
- timestamp;
- hostname or node allocation;
- compiler and compiler version;
- MPI implementation and version;
- loaded modules;
- build flags;
- input parameters;
- requested resources;
- runtime;
- correctness or convergence result;
- stdout path;
- stderr path;
- exit status.

Do not classify a job as successful based only on exit code.
Validate expected output and correctness criteria.

## Git policy

- Aspire2A should use a real Git clone of this repository at the remote project root.
- Manage the local PC clone and Aspire2A clone with this procedure:
  - Before starting work in either environment, run `git status` and `git pull --ff-only`.
  - Before committing, run `git status` and inspect the relevant diff.
  - Commit only reviewed/useful scripts, plans, progress notes, extracted results, metadata, and logs.
  - Prefer committing and pushing from the local PC.
  - After pushing from one environment, pull with `git pull --ff-only` in the other environment before continuing work there.
  - If `git pull --ff-only` fails because the clones diverged, stop and inspect instead of creating a merge commit.
- Useful failure records, patched scripts, and progress notes may be committed.
  Temporary files and irrelevant failed artifacts should not be committed.
- Local-to-Aspire2A script workflow:
  - When Codex creates or updates build scripts, PBS scripts, run scripts, extraction scripts, or planning files locally for remote execution, Codex must commit and push those local changes first, after user approval if required.
  - Before using those scripts on Aspire2A, Codex must SSH into Aspire2A, go to the remote project root, and run `git pull --ff-only`.
  - Do not run stale local-only scripts on Aspire2A. The remote clone should receive local script changes through Git before build/run work starts.
  - This rule covers the local PC to Aspire2A direction. Aspire2A to local result handling may use a separate workflow decided later.
- Prefer local Git operations.
- Do not store GitHub credentials on Aspire2A.
- Do not push without explicit user approval.
- Do not commit raw temporary files unless requested.

# Section start-up action

At the start of every session, read the latest progress report in ```/progress``` to get the context on what is completed and what we are doing next.

# Technical notes for workflow

## General notes (applied for all steps, unless specified otherwise)

- Naming convention:
  - Use one stable build or experiment name throughout the README, script
    names, PBS job names, output names, and build or binary paths.
  - Use kebab-case for directories, for example
    `CCE13-CrayMPICH8-newWF`.
  - Use lowercase snake_case for shell and PBS filenames, matching the
    existing scripts, for example `build_lulesh_newwf.pbs`.
  - Use `<name>_v1`, `<name>_v1.1`, and `<name>_v1-final` for attempts.
  - Use `<name>_v1.o` and `<name>_v1.e` for PBS output files.

- Script documentation and comments:
  - Every script must begin with a short comment describing its purpose,
    expected working directory, inputs, outputs, and important assumptions.
  - Divide scripts into clear, commented sections so the user can follow the
    workflow and make manual patches when needed.
  - Comments should explain purpose, reasoning, or non-obvious behavior. Do
    not add comments that merely restate obvious commands.

- Build `.sh` scripts should use this order:
  1. Shell safety settings.
  2. Build configuration and paths.
  3. Helper functions, if needed.
  4. Environment and tool checks.
  5. Source and build-directory checks.
  6. Configure command.
  7. Build command.
  8. Expected executable check.

- Build `.pbs` scripts should use this order:
  1. PBS job name, output/error paths, and resource requests.
  2. Shell safety settings.
  3. Change to the submitted script directory.
  4. Print or load the required environment.
  5. Call the corresponding build `.sh` script.

- Run `.pbs` scripts should use this order:
  1. PBS job name, output/error paths, and resource requests.
  2. Shell safety settings.
  3. Change to the submitted script directory.
  4. Define and print experiment metadata.
  5. Define and verify the successful build binary.
  6. Print the environment and tool versions.
  7. Execute the application through the required launcher.

- Keep build and run scripts consistent in shell options, comment style,
  metadata keys, variable naming, and attempt/output naming.

## Step 1: Planning
- We skip this step for now, the planning will be instructed by user right in the session

## Step 2: Preparing the build/run directories

- Prepare everything in the local repo in this PC first. The agent is allowed to ssh to Aspire2A to get information to prepare the scripts/debug, but refrain from editing the repo on Aspire2A.

### 2.1: Preparing the build directory
- Directory used: `builds/`: This directory contains build-related material for LULESH variants. The layout is as follows:

```text
builds/
├── source/
├── build-scripts/
└── extra-packages/
```

- More details on the directory:
  - `source/`: source code cloned or copied for building the application with
  different compilation methods.
  - `build-scripts/`: reusable build scripts kept for record and handoff.
  - `extra-packages/`: explicitly approved local dependencies or vendored packages, if needed.

- Do not install or modify shared software on Aspire2A. Prefer available modules.
- Ask for user approval before adding a new package that is not already available.

- Phase 1: Always do git clone on login node on Aspire2A using a direct command first before writing the build script and building. After that we use the path of the cloned source code to build. Do NOT clone the source on the local version of the repo on the PC. A note: if the source is already cloned and for the new build, the build guide of the application instruct that we only need to create a `build` directory in the source directory, do so instead.

- The preparation order is:
  1. Inspect Aspire2A and clone the application source on the login node.
  2. Prepare the build/run scripts and documentation in the local repository.
  3. Commit and push the local changes.
  4. Pull the changes on Aspire2A before submitting jobs.

- Phase 2: Preparation of the the build script in the `build-scripts/` directory
  - Create a separate directory in `build-scripts` for each build, name the directory something descriptive for the optimization - this will be used consistently across throughout the workflow. The structure will be as follows:

  ```text
  <build_name>/
  ├── README.md
  ├── <build_script.pbs>
  └── outputs/
  ```

  - More details on the directory:
    - `README.md`: A concise summary of the optimization for this build. Must include: (1) Concise summary, (2) compiler environment, (3) compiler used, (4) MPI compiler used, (5) Other optimization notes if applicable, and (6) Record of BUILD error-patching
    different compilation methods.
    - `<build_script.pbs>`: pbs build script to submit as batch job to execute the build
    - `outputs/`: Where to store the raw `.o` and `.e` files from the jobs for note-keeping purposes.

  - Build-script PBS output policy:
    - Keep all PBS `.o` and `.e` files for build jobs.
    - Direct build-job stdout/stderr into the `outputs/` directory inside the relevant build-script directory. No need to manually extract anything at this step
    - Use user-friendly output names such as `<build_name>_v1.o`, `<build_name>_v1.e`, `<build_name>_1.1.o`, `<build_name>_v1.1.e`, `<build_name>_v1-final.o`, and `<build_name>_v1-final.e` instead of opaque code-like names when practical.

  - Build README error-handling policy:
    - Use the build-script directory `README.md` to record build metadata, experiment intent, errors, and solutions. Record BUILD failures and patch attempts on an attempt-by-attempt basis.
    - After each failed build/run attempt, immediately update the relevant `README.md` with:
      - attempt label, such as `<build_name>_v1`, `<build_name>_v1.1`, or `<build_name>_v1-final`;
      - PBS job ID;
      - stdout and stderr paths;
      - observed error;
      - suspected cause;
      - patch or workflow change applied;
      - result of the next attempt, once known.
    - Do not wait until the end of a long debugging sequence to summarize errors. Record each attempt while the context is fresh.

### 2.2 Preparing the run directory

- Directory used: `experiments/`: This directory contains run-specific experiment folders. Each subdirectory should represent a specific optimization run or run family. Examples:

```text
experiments/
├── ICC25-O3/
└── ICC25-O2/
```

- Suggested contents for each experiment directory:

```text
experiments/<run_name>/
├── README.md
├── <run_script.pbs>
└── outputs/
```

- More details on the directory:
    - `README.md`: A concise summary of the optimization for this run. Must include: (1) Concise summary, (2) The successful run binary path, (3) compiler environment, (4) compiler used, (5) MPI compiler used, (6) Other optimization notes if applicable, and (7) Record of RUNTIME error-patching
    different compilation methods.
    - `<run_script.pbs>`: pbs run script to submit as batch job to execute the run
    - `outputs/`: Where to store the raw `.o` and `.e` files from the jobs for note-keeping purposes.

  - Run-script PBS output policy:
    - Keep all PBS `.o` and `.e` files for run jobs.
    - Direct run-job stdout/stderr into the `outputs/` directory inside the relevant directory. No need to manually extract anything at this step
    - Use user-friendly output names such as `<run_name>_v1.o`, `<run_name>_v1.e`, `<run_name>_1.1.o`, `<run_name>_v1.1.e`, `<run_name>_v1-final.o`, and `<run_name>_v1-final.e` instead of opaque code-like names when practical.

  - run README error-handling policy:
    - Use the run-script directory `README.md` to record run metadata, experiment intent, errors, and solutions. Record RUNTIME failures and patch attempts on an attempt-by-attempt basis.
    - After each failed run/run attempt, immediately update the relevant `README.md` with:
      - attempt label, such as `<run_name>_v1`, `<run_name>_v1.1`, or `<run_name>_v1-final`;
      - PBS job ID;
      - stdout and stderr paths;
      - observed error;
      - suspected cause;
      - patch or workflow change applied;
      - result of the next attempt, once known.
    - Do not wait until the end of a long debugging sequence to summarize errors. Record each attempt while the context is fresh.
  
  - Raw PBS output files stay in the `outputs/` directory. Extracted result files belong in `results/` (what to extract will be instructed later)

## Step 3: Sync the 2 repos in the local PC and on Aspire2A

- Sync the 2 repos, resolve any git-related issues in this step. Continue only with a clean tree.

## Step 4: Execute the build/run on Aspire2A

- After the build/run directories are created and prepared as detailed in Step 2, submit the build/run scripts as batch jobs and monitor the output and proceed accordingly according details in Step 2. Repeat the loop Step 2 to Step 4 until the build/run succeeds.
- Ensure the relevant `outputs/` directory exists on Aspire2A before submitting the PBS job.
- For a build, success requires:
  - the PBS job finishes successfully;
  - the expected output files are present in the designated `outputs/` directory; and
  - the expected executable is present.
- For a run, success requires:
  - the PBS job finishes successfully;
  - the expected output files are present in the designated `outputs/` directory; and
  - normal application output is present.
- Correctness validation is required before accepting benchmark results and will be handled in a later workflow stage.

## Step 5: Log results

- At the end of a build/run session, record results only. Do not perform
  optimization analysis or update planning conclusions in this step.

- The `results/` directory should contain:

```text
results/
├── README.md
├── metrics.csv
├── RESULTS.md
└── scripts/
```

- `results/README.md` must retain the directory description and usage guidance
  already documented in that file. It must also define the result data
  contract, including:
  - what one row in `metrics.csv` represents;
  - required columns and their meanings;
  - units and naming conventions;
  - how run status, failures, and repeated measurements are represented; and
  - which raw `.o` and `.e` files provide the source for each row.

- The CSV structure is application- and experiment-specific. Before each new
  optimization sweep, decide the required columns with the user and document
  the decision in `results/README.md`. New completed runs normally add rows.
  Add or change columns only after discussing and recording the schema change
  with the user.

- `metrics.csv` is the structured source of truth for extracted numeric and
  run metadata. Keep repeated runs as separate rows unless a different rule
  has been agreed and documented.

- `results/scripts/` contains scripts used to extract and transform values
  from raw experiment output. These scripts must follow the general script
  documentation and naming rules.

- Create or update `RESULTS.md` from `metrics.csv` after the CSV is prepared.
  `RESULTS.md` is the human-readable report and may contain tables, concise
  status summaries, correctness information, and links to raw output files.
  Its values must come from `metrics.csv`; it must not become an independent
  data source.

- Analysis is deferred to a later session. The user will instruct the agent
  when to copy or summarize results from `results/` into `planning/`. The
  results-logging session must not add interpretation, optimization decisions,
  or next-experiment conclusions to `planning/`.
