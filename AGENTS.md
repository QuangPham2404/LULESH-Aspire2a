# LULESH Project Workflow Instructions

This project uses the reusable Workflow v2 rules in `workflow/`, together with
the Aspire2A-specific restrictions and permissions in this file. The numbered
workflow files are authoritative for shared procedures; this file records
project-specific configuration, safety constraints, and command permissions.

## Required startup reading

Before workflow action, Codex must:

1. Read every numbered file in `workflow/` in numerical order.
2. Read `APPLICATION.md` and the latest progress report under `progress/`.
3. Check local Git state and synchronization according to
   `workflow/01-Git-Sync-Policy.md`.
4. For normal execution, identify the exact `tasks/TASK-XXX.md` named by the
   user, read it, and verify its status is `APPROVED` with `current_owner: codex`.
   Do not infer an active task from file timestamps, progress notes, or analysis.

The only no-task exception is the user's exact command `SETUP`; follow the
restricted procedure below. No other wording or workflow recommendation
activates that exception.

## Roles and authority

The authority flow is:

```text
Human Leader
    ↓
Strategic Analyst
    ↓
approved tasks/TASK-XXX.md
    ↓
Codex Orchestrator
    ↓
bounded execution workers
```

### Human Leader

The Human Leader owns approvals, strategic direction, resource and risk
decisions, final decisions, and changes in optimization direction.

### Strategic Analyst

The Strategic Analyst owns campaign-level interpretation, quantitative and
trend analysis, hypothesis generation and evaluation, causal reasoning,
experiment design, Strategic Specifications, and strategic analysis under
`planning/analysis/`. The analyst proposes work; the Human Leader approves it
through an approved task.

### Codex Orchestrator

Codex is the operational orchestrator, not the Strategic Analyst. It reads an
approved task, decomposes only its bounded work, coordinates workers when
available and permitted, performs operational validation, preserves evidence,
checks scope, and appends the `CODEX EXECUTION REPORT` to that task.

Codex must not choose campaign-level optimization direction, perform strategic
interpretation, rewrite the Strategic Specification, promote baselines, or
exceed approved task scope. Directly observed facts and mechanical derived
values may be reported without strategic conclusions.

### Bounded execution workers

Workers may inspect, probe, execute, test, modify explicitly approved files,
extract measurements, and preserve evidence only within the task's scope.
Worker authority never exceeds Codex authority or the approved task. Worker
communication is transient; do not create per-worker task or report files by
default. Follow the platform's applicable restrictions on delegation.

## `SETUP` exception

When the user invokes `SETUP`, Codex may proceed without an active task only to
follow this procedure:

1. **Read-only inspection and proposal:** inspect the local project and its
   workflow configuration; report the specific setup changes that appear
   necessary. Do not create, edit, delete, or otherwise modify files.
2. **User agreement:** wait for the user to agree to the proposed changes.
3. **Final confirmation:** present the concrete, bounded change set and wait
   for the user's final confirmation before applying it.
4. **Apply:** make only the changes included in that final confirmation and
   validate them within the confirmed scope.

`SETUP` does not authorize scientific execution, cluster jobs, optimization
experiments, strategic analysis, source changes, or changes beyond the final
confirmed setup scope. Any such work requires a separately approved task or
explicit authorization applicable under Workflow v2.

## Aspire2A configuration and safety

These project-specific values and restrictions must be preserved. Do not
replace them with placeholders:

- Cluster: Aspire2A.
- SSH alias: `aspire2a`.
- Persistent connection check before remote work: `ssh -O check aspire2a`.
- If the connection is unavailable, stop and ask the user to run
  `aspire2a-connect`. Do not initiate a normal interactive SSH login.
- Every Codex-controlled SSH command must use
  `ssh -o BatchMode=yes aspire2a '<command>'`.
- Every Codex-controlled SCP command must use `scp -o BatchMode=yes ...`.
- Every Codex-controlled rsync command must use
  `rsync -e 'ssh -o BatchMode=yes' ...`.
- Remote project root:
  `/home/users/ntu/pham0094/scratch/LULESH-Aspire2a`.
- Do not read, write, modify, or delete remote files outside that root without
  explicit user approval.
- Never request, read, store, transmit, echo, or log SSH passwords. Never use
  `sshpass`, Expect, password files, clipboard extraction, environment
  variables, or command-line password arguments; never automate password
  entry or modify SSH authentication settings.
- Do not use `sudo`. Do not install Codex, package managers, services,
  daemons, proxies, or remote agents. Do not install packages or modify shared
  software without explicit user approval; prefer available modules.
- Run computation through PBS batch jobs. Do not perform computational
  workloads on login nodes and do not poll PBS excessively.
- Do not delete files or folders without explicit user approval. Preserve
  pre-existing untracked files and runtime artifacts.

`workflow/00-General-SSH-Rules.md` is the shared cluster adapter. Its
placeholders must be completed before remote work; this project file does not
authorize bypassing that check. Keep the Aspire2A values above intact when the
adapter is completed.

## Project Git and synchronization rules

Follow `workflow/01-Git-Sync-Policy.md` plus these project restrictions:

- Aspire2A must use a real Git clone at the remote project root. Prefer local
  Git operations and do not store GitHub credentials on Aspire2A.
- Before work in either clone, run `git status` and `git pull --ff-only` as
  applicable. If fast-forward synchronization fails or clones diverge, stop
  and inspect; do not merge or overwrite changes automatically.
- Prepare scripts and documentation locally first. Before remote use, inspect
  the relevant diff, validate, commit and push only when authorized, then pull
  the reviewed commit on Aspire2A with `git pull --ff-only` and verify the
  intended task and script versions.
- Do not run stale local-only build, run, extraction, or planning scripts on
  Aspire2A. Never commit unrelated or unreviewed changes or raw temporary
  files unless requested.
- A push requires explicit user approval. Routine permission to run Git
  commands does not by itself authorize a push.

## LULESH-specific workflow constraints

- `APPLICATION.md` is the factual application overview. Keep optimization
  hypotheses, priorities, and conclusions in the Strategic Analyst's
  authorized planning work; Codex must not turn application setup or result
  logging into strategic analysis.
- The local repository must not be used to clone a new LULESH source tree.
  For source acquisition on Aspire2A, the existing project rule requires a
  direct source clone on the login node before preparing its build scripts,
  unless the upstream build guide only requires a build directory in an
  existing clone. This source-acquisition action still requires an approved
  task and the synchronization rules above.
- Keep established LULESH directory, attempt, PBS output, and script naming
  conventions from `workflow/02-Repo-Structure.md` and
  `workflow/03-Workflow-General-Notes.md`. Preserve every attempt's raw PBS
  `.o` and `.e` evidence under its designated `outputs/` directory; never
  overwrite it on retry.
- Result rows must retain experiment/build IDs, PBS job ID, timestamp,
  hostname/node, compiler and version, MPI implementation and version, loaded
  modules, build flags, inputs, requested resources, runtime, correctness,
  stdout/stderr paths, and exit status. Do not call a run successful from exit
  status alone; validate expected LULESH output and correctness markers.
- The existing `results/README.md` defines the metrics schema. Preserve it and
  append compatible attempts. Discuss and document any new columns, units, or
  result semantics with the Human Leader before changing the schema.
- A completed run with non-finite or failed scientific correctness (including
  `MaxRelDiff = -nan`) is not a workflow-patching opportunity by default.
  Preserve and log the result, record the correctness issue in
  `results/RESULTS.md`, and do not patch it without a separately authorized
  scope.
- Probes are observational. Keep their outputs in the designated output
  directory, do not include optimization recommendations or configuration
  changes, and preserve their raw PBS logs as tracked evidence. Include them
  in reviewed commits and push only with explicit user approval. Follow
  `workflow/04-Workflow-Probing-Scripts-Rules.md`.

## Error handling

Follow `workflow/05-Workflow-Error-Patching-Procedures.md` for classification,
evidence, retry, correctness, and patching. Additional project-specific
requirements:

- Track 2 manual-inspection cases belong in the append-only root
  `MANUAL_INSPECTION_ERROR.md`; preserve the case ID, status, evidence,
  unresolved questions, and user decision there.
- `OVERRID_AUTO_PATCH` authorizes only its explicitly named error class,
  allowed action, scope, and restrictions. It does not authorize unrelated
  changes, optimization decisions, authentication changes, destructive
  actions, or shared-software changes.

## Project command permissions

The following commands are permitted only when they are required by an
explicitly requested, approved task and stay within the paths and scope above.
This list is not an independent authorization to start work or expand a task.

### Local commands

- Read-only Git inspection: `git status`, `git diff`, and relevant Git
  inspection.
- `git pull --ff-only` for synchronization.
- `git add` and `git commit` for reviewed files belonging to the approved
  task, after inspecting the relevant diff and validating the changes.
- `git push origin <current-branch>` only with explicit user approval.
- Non-mutating checks such as `bash -n <project-script>`; `chmod +x` when
  required for a reviewed project script; and `mkdir -p` for designated
  project build, experiment, or output directories.
- Removal of generated temporary caches only where the authorized task
  requires it; the general deletion restriction still applies to other files
  and folders.

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
outside the approved task. Follow `workflow/06-Workflow-Automation-and-Authorization.md`.

## Workflow v2 references

Read and follow all numbered files, not only the file most relevant to the
immediate action:

| File | Authority |
| --- | --- |
| `workflow/00-General-SSH-Rules.md` | Shared SSH and cluster adapter; this project file supplies the Aspire2A values above, and remote work remains blocked while adapter placeholders are incomplete. |
| `workflow/01-Git-Sync-Policy.md` | Local/cluster synchronization, review, commit, push, and task-revision checks. |
| `workflow/02-Repo-Structure.md` | Canonical project layout, task-file contract, and build/run/results locations. |
| `workflow/03-Workflow-General-Notes.md` | Naming, script, preflight, metadata, and evidence conventions. |
| `workflow/04-Workflow-Probing-Scripts-Rules.md` | Probe scope, placement, output, and execution constraints. |
| `workflow/05-Workflow-Error-Patching-Procedures.md` | Track 1/2 errors, scientific correctness, and patch authorization. |
| `workflow/06-Workflow-Automation-and-Authorization.md` | Task-bounded command and action authority. |
| `workflow/07-Workflow.md` | End-to-end task lifecycle, execution report, results, analysis authorization, and handoff. |

For normal work, an approved, explicitly identified task is the execution
contract. A progress note, analysis recommendation, prior authorization, or
this project command-permission list cannot replace or expand that task.
