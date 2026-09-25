# LULESH Project Workflow Instructions

This project uses the reusable Codex HPC Optimization Workflow Pack v2 in
`workflow/`, together with the Aspire2A-specific restrictions and permissions
in this file. The numbered workflow files define shared procedures; this file
records the active application, cluster configuration, and project-specific
constraints.

## Required startup reading

Before normal workflow action, Codex must:

1. Read every numbered file in `workflow/` in numerical order.
2. Read `APPLICATION.md`.
3. Identify the exact `tasks/TASK-XXX.md` named by the user; do not infer the
   active task from file dates, progress notes, or analysis.
4. Read the approved task and the latest progress report under `progress/`.
   Verify front matter has `status: APPROVED` and `current_owner: codex`, and
   `### 1.11 Authorization` records `status: APPROVED`, `approved_by: user`,
   and the exact `approved_scope` before execution.
5. Check Git state and synchronization according to
   `workflow/01-Git-Sync-Policy.md`.

For the exact command `SETUP`, no active task or progress report is required.
Read `APPLICATION.md` if present, the complete workflow pack, and Git state;
inspect available project guidance and configuration; and follow the `SETUP`
procedure in `workflow/07-Workflow.md`. Do not modify files until the user
confirms the final, concrete change set. Normal approved-task startup applies
after setup.

## Roles and authority

### Human Leader

The Human Leader owns strategic direction, approvals, resource and risk
decisions, final decisions, and changes in optimization direction.

### Strategic Analyst

The Strategic Analyst owns raw-evidence interpretation, quantitative and
trend analysis, hypothesis generation and evaluation, causal reasoning,
experiment design, Strategic Specification creation, and authorized analysis
under `planning/analysis/`. The analyst proposes work; the Human Leader
approves it through an approved task.

The Strategic Analyst is normally ChatGPT Web / Sol. It drafts new tasks from
`workflow/TASK-TEMPLATE.md` for Human Leader review. With authorized direct
GitHub access, it may write a task after explicit human approval and write
analysis after `ANALYSE_RESULTS`. A conversation draft is a proposal, not
executable repository state. The Human Leader reviews and explicitly approves
each task before it is materialized. Otherwise the Human Leader writes the
approved task or authorizes a repository agent to copy its exact content
mechanically.

### Codex Orchestrator

Codex is the operational orchestrator, not the Strategic Analyst. It reads an
approved task from the synchronized repository, decomposes only its bounded
work, manages permitted workers, identifies parallel and dependent work,
performs bounded follow-up orchestration, validates evidence operationally,
checks scope compliance, and completes the `CODEX EXECUTION REPORT`.

Codex must not reconstruct a Strategic Specification from conversation
history, rewrite the specification, change the strategic objective, infer
campaign-level root cause, choose an optimization direction, promote
baselines, or exceed approved task scope. It may report directly observed
facts and mechanically derived values without strategic conclusions.

### Execution Workers

Workers may probe, inspect, execute, test, modify only within explicitly
approved scope, extract measurements, and preserve raw evidence. They may use
local reasoning needed to complete assigned work, but must not interpret
campaign-level results, recommend the next strategic action, or expand scope.
Worker authority never exceeds Codex authority or the approved task. Worker
communication is transient; do not create per-worker task or report files by
default. Follow the platform's applicable restrictions on delegation.

## Active project configuration

- Application: LULESH 2.x; see `APPLICATION.md`.
- Active cluster: Aspire2A.
- Workflow pack: `workflow/`.
- Application overview: `APPLICATION.md`.
- Active task: the exact `tasks/TASK-XXX.md` identified by the user.
- Remote project root:
  `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a`.

The remote project root and complete operational SSH configuration must also
be recorded in `workflow/00-General-SSH-Rules.md`. Preserve the project values
below when adapting or reviewing that file.

## Aspire2A configuration and safety

- SSH alias: `aspire2a`.
- Persistent connection check before remote work: `ssh -O check aspire2a`.
- If unavailable, stop and ask the user to run `aspire2a-connect`. Do not
  initiate a normal interactive SSH login.
- Every Codex-controlled SSH command must use
  `ssh -o BatchMode=yes aspire2a '<command>'`.
- Every Codex-controlled SCP command must use `scp -o BatchMode=yes ...`.
- Every Codex-controlled rsync command must use
  `rsync -e 'ssh -o BatchMode=yes' ...`.
- Do not read, write, modify, or delete remote files outside the project root
  without explicit user approval.
- Never request, read, store, transmit, echo, or log SSH passwords. Never use
  `sshpass`, Expect, password files, clipboard extraction, environment
  variables, or command-line password arguments. Never automate password
  entry or modify SSH authentication settings.
- Do not use `sudo`. Do not install Codex, package managers, services,
  daemons, proxies, or remote agents. Do not install packages or modify shared
  software without explicit user approval; prefer available modules.
- Run computation through PBS batch jobs. Do not perform computational
  workloads on login nodes or poll PBS excessively.
- Do not delete files or folders without explicit user approval. Preserve
  pre-existing untracked files and runtime artifacts.

## Task and project-specific automation permissions

An approved `tasks/TASK-XXX.md` defines the maximum execution scope for Codex.
Project permissions also define the allowed commands, paths, and restrictions.
Neither this file nor the reusable workflow pack independently authorizes
starting work or expanding a task.

Before execution, verify task front matter has `status: APPROVED` and
`current_owner: codex`, and `### 1.11 Authorization` records
`status: APPROVED`, `approved_by: user`, and the exact `approved_scope`
matching the user's instruction. The task must be synchronized and committed
to the repository; conversation drafts are proposals only.

### Git and synchronization

- Aspire2A must use a real Git clone at the remote project root. Prefer local
  Git operations and do not store GitHub credentials on Aspire2A.
- Before work in either clone, run `git status` and `git pull --ff-only` when
  synchronization is required. If fast-forward synchronization fails or the
  clones diverge, stop and inspect; do not merge or overwrite changes
  automatically.
- Prepare scripts and documentation locally first. Before remote use, inspect
  the relevant diff, validate, commit and push only when authorized, then pull
  the reviewed commit on Aspire2A with `git pull --ff-only` and verify the
  intended task and script versions.
- Do not run stale local-only build, run, extraction, or planning scripts on
  Aspire2A. Never commit unrelated or unreviewed changes or raw temporary
  files unless requested.
- A push requires explicit user approval. Routine Git permission does not
  authorize a push.

### Local commands

These commands are permitted only when required by an explicitly requested,
approved task and within its paths and scope:

- Read-only Git inspection, including `git status` and `git diff`.
- `git pull --ff-only` for synchronization.
- `git add` and `git commit` for reviewed files belonging to the approved
  task, after inspecting the relevant diff and validating changes.
- `git push origin <current-branch>` only with explicit user approval.
- Non-mutating checks such as `bash -n <project-script>`; `chmod +x` when
  required for a reviewed project script; and `mkdir -p` for designated
  project build, experiment, or output directories.
- Removal of generated temporary caches only when the authorized task
  requires it; the general deletion restriction applies to other files and
  folders.

### Remote commands

- `ssh -O check aspire2a` before remote work.
- Non-interactive SSH inspection, approved-root Git synchronization, PBS
  submission, bounded `qstat` monitoring, and project-root workflow operations
  using the required SSH form above.
- `scp -o BatchMode=yes ...` to retrieve generated outputs into their matching
  local project directories.
- `qsub` for reviewed build, run, or read-only probe scripts explicitly
  covered by the approved task.

These permissions do not authorize `qdel`, package installation, shared
software changes, source-code changes, optimization decisions, resource-policy
changes, authentication changes, deletion, external coordination, or actions
outside the approved task. Follow
`workflow/06-Workflow-Automation-and-Authorization.md`.

## LULESH-specific workflow constraints

- `APPLICATION.md` is the factual application overview. Keep optimization
  hypotheses, priorities, and conclusions in the Strategic Analyst's
  authorized planning work; Codex must not turn application setup or result
  logging into strategic analysis.
- Do not clone a new LULESH source tree into the local repository. For source
  acquisition on Aspire2A, follow the existing project rule requiring a direct
  source clone on the login node before preparing build scripts, unless the
  upstream build guide only requires a build directory in an existing clone.
  Source acquisition still requires an approved task and the synchronization
  rules above.
- Follow the established LULESH directory, attempt, PBS output, and script
  naming conventions in `workflow/02-Repo-Structure.md` and
  `workflow/03-Workflow-General-Notes.md`. Preserve every attempt's raw PBS
  `.o` and `.e` evidence under its designated `outputs/` directory; never
  overwrite evidence on retry.
- Result rows must retain experiment/build IDs, PBS job ID, timestamp,
  hostname/node, compiler and version, MPI implementation and version, loaded
  modules, build flags, inputs, requested resources, runtime, correctness,
  stdout/stderr paths, and exit status. Do not call a run successful from exit
  status alone; validate expected LULESH output and correctness markers.
- Preserve the schema in `results/README.md` and append compatible attempts.
  Discuss and document new columns, units, or result semantics with the Human
  Leader before changing the schema.
- A completed run with non-finite or failed scientific correctness, including
  `MaxRelDiff = -nan`, is not a workflow-patching opportunity by default.
  Preserve and log the result, record the correctness issue in
  `results/RESULTS.md`, and do not patch it without separately authorized
  scope.
- Probes are observational. Keep outputs in the designated output directory;
  include no optimization recommendations or configuration changes; and
  preserve raw PBS logs as tracked evidence. Follow
  `workflow/04-Workflow-Probing-Scripts-Rules.md`. Push probe changes only with
  explicit user approval.

## Error handling

Follow `workflow/05-Workflow-Error-Patching-Procedures.md` for classification,
evidence, retry, correctness, and patching. Additional project requirements:

- Track 2 manual-inspection cases belong in the append-only root
  `MANUAL_INSPECTION_ERROR.md`; preserve the case ID, status, evidence,
  unresolved questions, and user decision.
- `OVERRID_AUTO_PATCH` authorizes only its explicitly named error class,
  allowed action, scope, and restrictions. It does not authorize unrelated
  changes, optimization decisions, authentication changes, destructive
  actions, or shared-software changes.

## Application-specific instructions

Maintain `APPLICATION.md` as the factual LULESH overview, including its source
URL and revision, purpose, dependencies, build/run commands, important inputs,
expected output markers, correctness criteria, and baseline command. Keep
optimization plans and conclusions under `planning/`.

## Conflict and stop rule

If instructions conflict, a required value is missing, the active task is not
approved, required authority is absent, or an error requires judgment beyond
the documented automatic track, stop the affected workflow and report what
must be resolved. Preserve evidence. Strategic analysis begins only after the
Human Leader explicitly authorizes `ANALYSE_RESULTS`.

## Workflow v2 references

Read and follow every numbered file, not only the one most relevant to the
immediate task:

| File | Authority |
| --- | --- |
| `workflow/00-General-SSH-Rules.md` | Shared SSH rules and active Aspire2A adapter. |
| `workflow/01-Git-Sync-Policy.md` | Local/cluster synchronization, review, commit, push, and task-revision checks. |
| `workflow/02-Repo-Structure.md` | Canonical project layout, task-file contract, and build/run/results locations. |
| `workflow/03-Workflow-General-Notes.md` | Naming, scripts, preflight, metadata, and evidence conventions. |
| `workflow/04-Workflow-Probing-Scripts-Rules.md` | Probe scope, placement, output, and execution constraints. |
| `workflow/05-Workflow-Error-Patching-Procedures.md` | Track 1/2 errors, scientific correctness, and patch authorization. |
| `workflow/06-Workflow-Automation-and-Authorization.md` | Task-bounded command and action authority. |
| `workflow/07-Workflow.md` | End-to-end task lifecycle, SETUP, execution report, analysis authorization, and handoff. |

For normal work, an approved, explicitly identified task is the execution
contract. Progress notes, analysis recommendations, prior authorization, and
the project command-permission list cannot replace or expand that task.
