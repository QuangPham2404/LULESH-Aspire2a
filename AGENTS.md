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

  `aspire2a-connect`

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

- After reading `AGENTS.md` at the start of each session, inform the user as confirmation.
- At the start of every session, read the latest progress report in ```/progress``` to get the context on what is completed and what we are doing next.

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

- Before configuring or running, scripts must fail clearly if required source
  paths, output directories, tools, launchers, or expected binaries are
  missing. A tool check must be fatal when that tool is required by the next
  command; reporting it as missing and continuing is not sufficient.
- A preflight requirement is mandatory only when the subsequent build, run, or validation command directly depends on that tool or its output. Tools used
  only for optional diagnostics or provenance must not block execution. If such a tool is unavailable, record unknown or emit a warning and continue when
  the primary workflow remains valid.
- Do not introduce new fatal preflight requirements by inference. When a check is not clearly required by the build/run command, treat it as optional or ask
  the user before making it mandatory.

## Rule for probing scripts

- A probing script is limited to observing hardware, software, modules,
  scheduler allocations, filesystem state, or other settings relevant to
  optimization strategy. It is unrelated to build, run, or results handling.
- Store probing scripts in `scripts/` with a clear lower-snake-case name and
  the same documentation, shell-safety, and PBS conventions as other scripts.
- Probing scripts may write raw output only to the relevant `outputs/`
  directory, normally `scripts/outputs/`. They must not edit source code,
  build, experiment, or results files; change shared settings; install
  software; or delete files.
- Probing scripts must not expose passwords, tokens, or sensitive environment
  variables. They must use bounded PBS resources and must not perform
  computational workloads on login nodes.
- Raw probe `.o` and `.e` files are required evidence. Keep them beside the
  relevant script, use a new attempt-specific name for every rerun, and commit
  and push them to GitHub like build and run output.
- Probe-only scripts may be committed, pushed, and submitted without separate
  permission when they satisfy the read-only scope above and pass syntax and
  output-path checks. They must still follow the normal synchronize, pull,
  submit, validate, and output-retrieval workflow.
- A probe may report facts relevant to optimization, but must not contain
  optimization recommendations or edit files based on them. Any script that
  suggests or applies an optimization, or otherwise writes outside its output
  directory, requires user permission before use.

## Error-patching procedures

- Classify build and run errors after inspecting the available evidence, not from
  the process exit status alone. Review the PBS state and exit status, stdout,
  stderr, expected output files, normal application output, and correctness or
  convergence markers before selecting an error-handling track.

### Track 1: automatic workflow patching

- Use Track 1 only for deterministic, low-risk defects in the workflow
  machinery. The cause must be sufficiently clear and the expected behavior
  after the correction must be unambiguous.
- Typical Track 1 errors include:
  - an incorrect working directory or relative path;
  - missing preparation of a designated output directory;
  - incorrect PBS output names or paths;
  - a stale or incorrect expected-binary path;
  - shell quoting or control-flow errors;
  - an unnecessarily strict preflight check;
  - inconsistent workflow metadata; and
  - an extraction-script parsing or duplicate-handling defect.
- Track 1 is limited to reversible changes to workflow scripts,
  documentation, metadata, and output handling. It must not be used when the
  correction requires source-code changes, optimization decisions, new
  compiler or MPI strategies, changed resource policies, shared-software
  changes, or an uncertain interpretation of application behavior.
- The build-specific and run-specific error-handling instructions later in
  this workflow remain authoritative for their respective operations. The
  agent must follow those sections for the additional build/run details,
  including the appropriate README, output directory, attempt naming,
  synchronization, validation, and success criteria.
- For a Track 1 failure, follow this procedure:
  1. Identify the error and confirm that it is a deterministic workflow defect.
  2. Preserve the failed attempt's evidence.
  3. Before applying a patch, immediately record the failed attempt in the
     corresponding build or experiment README. Include the attempt label, PBS
     job ID, stdout path, stderr path, observed error, suspected cause, and
     planned patch.
  4. Apply the patch in the local repository and perform appropriate checks,
     such as shell syntax, path, or configuration validation.
  5. Use a new attempt label and new PBS `.o` and `.e` filenames. Never
     overwrite the earlier attempt's evidence.
  6. Follow the Git and synchronization procedure before using changed
     scripts on Aspire2A: review the local changes, commit and push when
     required, then pull the reviewed changes remotely with
     `git pull --ff-only`.
  7. Submit the retry through PBS and update the corresponding README with
     the result of the retry.
  8. Continue the normal build/run validation workflow. A retry is successful
     only when the applicable PBS, output-presence, application-output, and
     correctness criteria are satisfied.
- Build failures and their Track 1 patches belong in
  `builds/build-scripts/<build_name>/README.md`. Run failures and their Track 1
  patches belong in `experiments/<run_name>/README.md`.

### Track 2: manual inspection

- Use Track 2 when the error requires interpretation, user judgment, external
  authorization, or a change beyond routine workflow repair.
- Typical Track 2 errors include:
  - compiler errors involving source compatibility or language behavior;
  - unavailable dependencies, packages, or modules;
  - MPI initialization failures, hangs, or abnormal termination;
  - scheduler, resource, hardware, or filesystem problems;
  - possible compiler or MPI correctness issues;
  - required changes to source code, inputs, compiler flags, resources, or
    launch strategy;
  - uncertain causes with multiple plausible explanations; and
  - repeated failure after a reasonable Track 1 patch.
- For a Track 2 failure, follow this procedure:
  1. Identify and classify the error.
  2. Preserve the evidence, including the experiment or build ID, attempt
     label, PBS job ID, timestamp, PBS state and exit status, allocated
     hostname or node, stdout and stderr paths, compiler and MPI metadata,
     loaded modules, flags, inputs, requested resources, and relevant
     application output.
  3. Stop the affected workflow. Do not patch, retry, change configuration,
     or submit another job automatically.
  4. Inspect the evidence without modifying the affected workflow.
  5. Record the observed error, suspected causes, confirmed facts,
     unresolved questions, affected build or run, and relevant evidence.
  6. Suggest one or more possible fixes for the user's manual review. A
     suggested fix is not authorization to apply it.
  7. Record the case in the root `MANUAL_INSPECTION_ERROR.md`.
  8. Wait for the user's decision or an explicitly scoped
     `OVERRID_AUTO_PATCH` authorization.
  9. After the issue is resolved or an authorized action is taken, update the
     same case with the selected fix, authorization or user decision, action
     taken, resulting attempt, outcome, remaining concerns, and final status.
- Maintain `MANUAL_INSPECTION_ERROR.md` as an append-only case log. Give each
  case a unique case ID and a status such as `OPEN`,
  `USER_ACTION_REQUIRED`, `AUTHORIZED_FOR_PATCH`, `RESOLVED`, or `CLOSED`.
- Recording a proposed fix in `MANUAL_INSPECTION_ERROR.md` never authorizes
  the agent to apply it.

### Scientific-correctness exception

- A build or run that completes but reports failed, non-finite, or otherwise
  invalid scientific correctness is handled as a special non-blocking case by
  default. Examples include `MaxRelDiff = -nan`, failed convergence, failed
  verification markers, or unexpected numerical output despite a successful
  process exit.
- Do not self-patch a scientific-correctness error by default. Continue the
  normal results workflow, preserve the attempt, and record its correctness
  status accurately.
- Add a clear note to `results/RESULTS.md` describing the affected run or
  attempt, the observed correctness failure, the relevant output marker, that
  no patch was attempted, and that further investigation is required.
- If the user later requests investigation or authorizes a patch, create or
  link a manual-inspection case as appropriate and follow the user's explicit
  scope.

### `OVERRID_AUTO_PATCH` authorization

- `OVERRID_AUTO_PATCH` is a user-supplied, command-like authorization that
  permits the agent to handle a named Track 2 error automatically.
- Use the following structured format:

  ```text
  OVERRID_AUTO_PATCH
  error_class: <specific error class>
  allowed_action: <specific permitted action>
  scope: <current attempt | current build | current experiment | current session>
  restrictions: <limitations>
  ```

- The override must explicitly name the error class, permitted action, scope,
  and applicable restrictions. An ambiguous override does not activate
  automatic patching.
- The override expires at the end of its stated scope. It authorizes only the
  named class of fix and does not authorize unrelated source changes,
  optimization decisions, resource changes, authentication changes, or
  destructive actions.
- Package or module actions must preserve compiler, MPI, module, package, and
  version provenance. Do not modify shared software unless that specific
  action is explicitly authorized and permitted by the operating rules.
- Record the override text or its essential authorization details, the matched
  error, action taken, environment or package changes, retry attempt, and
  result in the applicable README and, for a Track 2 case, in
  `MANUAL_INSPECTION_ERROR.md`.

## Standing automation authorization

The user authorizes routine commands required by the explicitly requested
LULESH workflow without asking for separate confirmation for each command.
This authorization applies only within the local repository and the approved
Aspire2A project root.

### Authorized routine local commands

- `git status`, `git diff`, and relevant read-only Git inspection;
- `git add` for reviewed files belonging to the current workflow;
- `git commit` for reviewed scripts, plans, progress notes, metadata, logs,
  and extracted results;
- `git pull --ff-only` to synchronize the Aspire2A clone;
- `git push origin <current-branch>` for commits produced by the current
  explicitly requested workflow;
- `bash -n <project-script>` and other non-mutating syntax checks;
- `chmod +x <project-script>` when required to execute a reviewed script;
- `mkdir -p` for designated build, experiment, and output directories;
- removal of generated temporary cache files such as
  `results/scripts/__pycache__/`.

### Authorized routine remote commands

- `ssh -O check aspire2a` before remote work;
- `ssh -o BatchMode=yes aspire2a '<command>'` for inspection, Git
  synchronization, PBS submission, bounded PBS monitoring, and project-root
  workflow operations;
- `scp -o BatchMode=yes ...` for retrieving generated build/run outputs into
  the matching local project directories;
- `qsub` for reviewed PBS build, run, and read-only probe scripts;
- bounded `qstat` inspection for submitted jobs and their recorded evidence.

### Authorization limits

- All SSH commands must remain non-interactive and use the persistent
  connection. Never request, read, store, transmit, or echo passwords or
  other authentication secrets.
- Remote commands must remain within
  `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a` unless the user gives
  explicit approval for a different path.
- This authorization does not cover destructive commands, `qdel`, shared
  software changes, package installation, authentication changes, source-code
  changes, optimization decisions, resource-policy changes, new external
  coordination, or unrelated files.
- Before committing, inspect the relevant diff and run appropriate validation.
  Do not push unrelated or unreviewed changes.
- If a command requires new authority, accesses a path outside the approved
  roots, or falls outside the current requested workflow, stop and ask the
  user.

## Step 1: Initial Planning
- At the start of work on a new application, create the root project
  `APPLICATION.md`. If it already exists, review and update it; do not recreate or
  overwrite it.
- The root `APPLICATION.md` is strictly an application overview, not an
  optimization plan. Optimization decisions, experiment priorities, and
  conclusions belong in `planning/`.
- The overview should contain:
  - the application GitHub link and the exact source revision or tag used;
  - a summary of what the application does and the scientific or functional
    correctness metrics it reports;
  - build dependencies and a concise guide to the key manual build commands;
  - key run commands, important input flags, and expected output markers;
  - the baseline command and expected correctness/output markers to establish
    before optimization runs begin.
- Step 1 documentation must be prepared in the local repository first, then
  committed and synchronized before remote build or run execution.
- The aim is to establish an overview understanding of the project before
  execution. Further planning is user-directed and belongs in `planning/`.
: Preparing the build/run directories

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
    - Do not create a separate `records/` directory for new builds. PBS
      stdout and stderr are the authoritative raw build records and must
      contain the build metadata, environment, commands, and errors needed for
      later validation.
    - Use a new attempt-specific output name for every rerun; do not overwrite
      an earlier `.o` or `.e` file.

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

  - Existing historical `records/` directories may be retained, but new
    workflow runs must not depend on or create them.

## Step 3: Sync the 2 repos in the local PC and on Aspire2A

- Before execution, check the status of both clones and synchronize the
  Aspire2A clone with `git pull --ff-only` after local script changes have
  been pushed.
- Continue only when synchronization succeeds, the intended commit is present
  in both clones, and neither tree has unexpected changes. Output files and
  other explicitly documented runtime artifacts are exempt from the clean-tree
  check.
- Verify that the submitted scripts and source revision are the versions
  reviewed for the current build/run attempt. If fast-forward synchronization
  fails or the clones diverge, stop and inspect the difference before running.

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
- Record the returned PBS job ID, submission and completion timestamps, final
  PBS state, PBS exit status, allocated hostname/node, and stdout/stderr paths.
- Validate application-specific success using expected output markers and
  correctness or convergence fields, including defined acceptance criteria
  where applicable. Do not classify a run as successful from PBS exit status or
  output-file presence alone.
- Use a new attempt label and output filename for every retry. Record failed
  attempts before applying a patch or submitting the next attempt.

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

- The CSV structure is application- and experiment-specific. Before a new
  optimization sweep, decide the required columns with the user and document
  the decision in `results/README.md`. Once a schema has been decided, runs
  that fit the existing schema may proceed automatically and normally add
  rows. Pause for user input only when new columns, units, or result semantics
  are needed. Add or change columns only after discussing and recording the
  schema change with the user.

- `metrics.csv` is the structured source of truth for extracted numeric and
  run metadata. Keep repeated runs as separate rows unless a different rule
  has been agreed and documented.
- Required workflow probe and PBS `.o`/`.e` logs are tracked and pushed as
  evidence. Only temporary or explicitly irrelevant raw artifacts should be
  excluded.
- Before extraction, confirm that the expected experiment output and required
  result fields are present in the designated output files. Step 5 does not
  need to recheck PBS job state or exit status.
- Result extraction must preserve existing rows, append new attempts, and
  reject or safely ignore duplicate `(experiment_id, attempt)` records. It
  must support recording failed or incomplete attempts when the available
  metadata permits, rather than assuming every extracted run succeeded.

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

## Step 6: Update results with analysis to planning/ and conduct analysis

Step 6 is a user-triggered analysis workflow. It begins only when the user
provides the command-like authorization `ANALYSE_RESULTS`. This authorization
permits the agent to read the recorded results, create or update analysis
documents under `planning/analysis/`, update the planning master tracker, and
present the selected data and analysis to the user. It does not authorize
submitting jobs, changing source code, changing build or run configuration,
applying optimization decisions, or starting the next experiment.

### `ANALYSE_RESULTS` authorization

The preferred form is:

```text
ANALYSE_RESULTS
analysis_id: <stable analysis name>
source: results/metrics.csv
include: <experiments, variants, or attempts to include>
grouping: <optimization direction or grouped tests>
scope: <current analysis | current session>
restrictions: <additional limits>
```

The `analysis_id` should be stable and use lowercase kebab-case, for example
`cce13-openmp-scaling`. `source` defaults to `results/metrics.csv`. The
`include` and `grouping` fields identify which CSV rows belong in the analysis
and how they should be compared. If the user supplies only
`ANALYSE_RESULTS`, the agent must inspect the available results and ask the
user which optimization direction or result group to analyze before writing a
new analysis document.

The command is scoped to the current user-requested analysis. It does not
authorize unrelated analysis files or automatic traversal of every result
unless the user explicitly requests that scope.

### Analysis directory and master tracker

Use this structure:

```text
planning/
├── README.md
├── PLANS.md
└── analysis/
    ├── <analysis-id>.md
    └── ...
```

`planning/PLANS.md` is the master tracker for the optimization workflow. It
must remain concise and must not become a duplicate of the complete result
data or detailed analysis. Its structure is fixed and consists of exactly
these three main sections:

1. `## Current baseline`: record the currently accepted reference
   environment, source revision, build and effective flags, workload, resource
   configuration, runtime/FOM, and correctness result. Update this section
   only when the project explicitly establishes a new baseline; do not replace
   the historical result rows in `results/metrics.csv`.
2. `## Optimization directions`: maintain one tracking-table row for each
   optimization direction. The table must include the direction, analysis ID
   and link, analysis date, analysis scope, status, main finding, and suggested
   follow-up. This table is also the analysis history, so do not maintain a
   separate `Analysis history` section in `PLANS.md`. When an analysis file is
   created or updated, add or update its row rather than copying the detailed
   analysis into the tracker. Preserve links to older analysis files when a
   direction is split into multiple related analyses.
3. `## Next direction`: record the single next optimization direction agreed
   from the `## 5. Suggested next section` of the latest relevant analysis
   file. Include the analysis-file link, hypothesis or purpose, required
   controls/repetitions, and success criteria when they are stated. This
   section is a planning record, not authorization to submit jobs or modify
   workflow files.

The required tracker table should have this shape:

```markdown
| Direction | Analysis ID / file | Analysis date | Scope | Status | Main finding | Suggested follow-up |
| --- | --- | --- | --- | --- | --- | --- |
```

Every authorized `ANALYSE_RESULTS` request must update the applicable row and
the `Next direction` section after the detailed analysis is written. The
tracker must distinguish provisional, scope-limited, invalid, completed, and
user-approved directions where applicable.

Each optimization direction has its own file under `planning/analysis/`.
Separate related tests into clearly labeled subsections within that file. If
one direction becomes too large or contains genuinely independent questions,
create additional analysis files with distinct stable IDs and link them from
the master tracker.

### Analysis source, data handling, and provenance

`results/metrics.csv` remains the structured source of truth. `RESULTS.md`
remains the generated human-readable results report. An analysis document may
copy the selected rows or a relevant table of fields from `metrics.csv` so
that the comparison is readable, but it must not silently alter, replace, or
become an independent source of numeric truth.

For every included result, preserve enough provenance to locate the source
row and raw evidence. At minimum, record the `experiment_id` and `attempt`;
when relevant, also include the PBS job ID, source commit, build flags, input,
MPI/task/thread configuration, runtime, FOM, correctness status, and links to
the run and build stdout/stderr files. Do not omit failed or scientifically
invalid results when they are relevant to the analysis. Explain why they are
excluded from valid-winner selection.

Before analyzing, confirm that the requested rows exist, the CSV schema is
unchanged or compatible, and the selected rows have the expected result
fields. Do not invent missing measurements. Mark unavailable values and
uncertain conclusions explicitly.

### Required analysis-file format

Every new or substantially updated analysis file must use the following
sections:

```markdown
# Analysis: <optimization direction>

## 1. Concise summary

What was tried, why it was tried, and the scope of this analysis.

## 2. Scope and evaluation criteria

Record the source revision, compiler/MPI environment, workload, baseline,
correctness requirements, performance metrics, included experiments, and
exclusions.

## 3. Data and analysis

Use clearly labeled subsections for each grouped test. Present the selected
data in tables or concise excerpts, followed by an interpretation of that
group. Values must agree with `results/metrics.csv`.

## 4. Insights gained

Record confirmed wins, regressions, invalid or inconclusive results, noise,
reproducibility limits, and other constraints.

## 5. Suggested next section

State the proposed next optimization direction, hypothesis, configurations,
required controls or repetitions, success criteria, and unresolved questions.

## 6. Provenance

Link to the source CSV, experiment IDs and attempts, raw output files, and
record the analysis date.
```

The exact headings may include descriptive text, but the six required content
areas must remain identifiable: concise summary; scope and evaluation criteria;
data and analysis; insights; suggested next section; and provenance. The
suggested next section is a recommendation for user review, not permission to
execute it.

### Analysis procedure

For an authorized `ANALYSE_RESULTS` request:

1. Read the current `results/README.md`, `results/metrics.csv`, and
   `results/RESULTS.md`, then identify the requested rows and their raw
   evidence.
2. Check correctness and validity before ranking performance. Correctness,
   finite numerical fields, and the documented acceptance criteria take
   precedence over runtime and FOM.
3. Copy the selected data needed for the comparison into the relevant
   `planning/analysis/<analysis-id>.md` file, retaining row identity and
   provenance links.
4. Analyze wins, regressions, failures, weak or strong scaling implications,
   timing noise, resource effects, and unresolved limitations as applicable.
5. Record a cautious, evidence-based suggested next section. Do not turn a
   single noisy or warning-affected measurement into a definitive conclusion.
6. Create or update the corresponding entry and link in `planning/PLANS.md`.
7. Present the selected data, analysis, limitations, and suggested next
   section to the user. The final response must be understandable without
   opening the analysis file.

The analysis workflow should preserve existing analysis history. When new
measurements are added later, update the affected analysis file with a new
analysis date and explain what changed; do not overwrite prior evidence or
silently rewrite an earlier conclusion.

## Step 7: Repeat the loop

There are 2 cases in which the workflow ends at the end of a session:

- (1) The the workflow stops before step 5, meaning errors/issues (eg. build/run errors, sudden ssh problems, etc) are preventing the runs to obtain acceptable results. In this case, the user will:
  1. Instruct the agent to end the session by writing the .md progress logging file into `progress` for that section.
  2. To continue for the next session, the user will instruct the agent to read the progress logs to continue debugging the issues. The workflow picks up on whatever step it was in the previous session.
- (2) The workflow completes until step 6, meaning results are logged and analysis are done. In this case the user will:
  1. Instruct the agent to end the session by writing the .md progress logging file into `progress` for that section.
  2. To continue for the next session, the user will work with the agent to investigate the analysis/insights for the previous session already available in the analysis file in `planning/analysis`. After deciding on the next optimization, the user will manually instruct the agent to update the same file in the `5. Suggested next section` with details for the next session and use that to plan the execution.
  3. From there, the workflow re-start from step 2.
