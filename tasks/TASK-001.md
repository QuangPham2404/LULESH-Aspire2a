---
task_id: TASK-001
title: Controlled OpenMP Affinity and Repeatability Validation
status: EXECUTING
current_owner: codex
parent_task: none
analysis_id: omp-affinity-repeatability
created: 2026-09-26
last_updated: 2026-09-26
---

# TASK-001 — Controlled OpenMP Affinity and Repeatability Validation

## 1. STRATEGIC SPECIFICATION

### 1.1 Objective

Validate whether the existing **1 MPI rank × 8 OpenMP thread** CCE13/O3 LULESH configuration remains consistently faster than the **1 MPI rank × 1 OpenMP thread** baseline when CPU/thread placement is explicitly verified and both configurations are measured repeatedly under controlled resources.

This task is a validation task, not a new optimization sweep.

### 1.2 Context

The current LULESH baseline and candidate use:

- source revision: `3e01c40b3281aadb7f996525cdd4a3354f6d3801`;
- compiler environment: Cray CCE 13.0.2;
- MPI: Cray MPICH 8.1.15;
- existing Release binary with effective flags `-fopenmp -O3 -DNDEBUG`;
- workload: `-s 30`;
- one MPI rank.

The current 1-thread baseline is approximately `20 s`.

The existing 8-thread run recorded:

- elapsed time: `6.6 s`;
- FOM: `3784.5446`;
- finite `MaxRelDiff = 1.461140e-12`;
- correctness passed.

This is approximately a 3× measured elapsed-time improvement over the 1-thread baseline.

However, the existing OpenMP runs emitted the Cray warning:

> Requested total thread count and/or thread affinity may result in oversubscription of available CPU resources.

The current OpenMP comparison also has only one recorded performance attempt per configuration. Therefore, the existing 8-thread result is a provisional candidate rather than a reproducible final selection.

Relevant prior analysis:

- `planning/analysis/initial_sweep.md`
- `planning/PLANS.md`

Relevant existing experiment:

- `experiments/CCE13-CrayMPICH8-baseline-s30-omp-sweep/`

### 1.3 Strategic Question / Hypotheses

**Strategic question**

Under verified CPU/thread placement and controlled resources, is the existing **1 MPI × 8 OpenMP** CCE13/O3 configuration consistently faster than the **1 MPI × 1 OpenMP** baseline for LULESH `-s 30`, while preserving scientific correctness?

**Working hypotheses**

1. The 8-thread configuration will remain substantially faster than the 1-thread baseline when placement is explicitly controlled.
2. The previous Cray warning reflects unverified affinity/placement rather than proof that the 8-thread measurement is invalid.
3. Repeated controlled measurements will determine whether the existing 6.6 s result is representative or unusually favorable.

These are hypotheses for later Strategic Analyst evaluation. Codex and execution workers must not decide whether they are confirmed.

### 1.4 Required Evidence / Deliverables

Collect **three controlled repetitions for each configuration**:

- 1 MPI rank × 1 OpenMP thread: 3 attempts;
- 1 MPI rank × 8 OpenMP threads: 3 attempts.

Target submission sequence:

```text
1T
8T
1T
8T
1T
8T
```

Exact scheduler completion order does not need to match submission order.

For every attempt, preserve and record:

- experiment ID and attempt ID;
- PBS job ID;
- submission/completion information where available;
- allocated node;
- requested PBS resources;
- exact binary path;
- source revision;
- compiler/MPI/module metadata;
- workload;
- MPI rank count;
- `OMP_NUM_THREADS`;
- affinity/binding-related environment used;
- actual thread-placement evidence;
- elapsed time;
- FOM;
- scientific correctness fields including `MaxRelDiff`;
- run/correctness status;
- stdout path;
- stderr path;
- exit status.

Each repetition must remain a separate raw attempt and a separate `results/metrics.csv` row.

Codex may calculate mechanical summary values such as:

- mean;
- minimum;
- maximum;
- standard deviation;
- percentage differences.

These derived values are operational summaries only. Codex must not conclude which configuration should become the new baseline.

### 1.5 Relevant Inputs and References

Existing binary:

```text
/home/users/ntu/pham0094/scratch/LULESH-Aspire2a/builds/source/LULESH-newWF/build-CCE13-CrayMPICH8-newWF-Release/lulesh2.0
```

Existing OpenMP experiment:

```text
experiments/CCE13-CrayMPICH8-baseline-s30-omp-sweep/
```

Existing runner:

```text
experiments/CCE13-CrayMPICH8-baseline-s30-omp-sweep/run_lulesh_cce13_omp.pbs
```

Existing evidence and planning:

```text
planning/PLANS.md
planning/analysis/initial_sweep.md
results/metrics.csv
results/RESULTS.md
```

The existing Cray warning identifies:

```text
CRAY_OMP_CHECK_AFFINITY=TRUE
```

as an available mechanism for detailed thread-affinity diagnostics.

`OMP_WAIT_POLICY` must not be treated as affinity validation merely because setting it may suppress the warning.

### 1.6 Execution Scope

#### Allowed

Codex may:

- inspect the existing CCE13/O3 build, OpenMP experiment, scripts, raw evidence, and result schema;
- inspect the relevant Aspire2A runtime and OpenMP affinity environment using bounded read-only commands;
- determine the minimal appropriate OpenMP/Cray affinity controls needed to establish explicit placement;
- use `CRAY_OMP_CHECK_AFFINITY=TRUE` or equivalent supported runtime diagnostics to record actual thread placement;
- create a new experiment directory dedicated to this controlled validation;
- create or modify task-specific PBS/run scripts and experiment documentation;
- use the existing CCE13/O3 binary without rebuilding it;
- submit the six approved benchmark attempts through PBS;
- perform bounded monitoring according to project policy;
- use the same controlled PBS allocation for both configurations where operationally valid;
- use an allocation of one node, one MPI rank, eight CPUs, and the existing memory scale for both configurations so that the scheduler resource envelope remains comparable;
- configure the 1-thread case to use one OpenMP thread within that allocation;
- configure the 8-thread case to use eight OpenMP threads within that allocation;
- verify that the 8-thread case places its OpenMP threads on distinct allocated CPU resources without unintended oversubscription;
- retrieve and preserve stdout/stderr;
- append compatible result rows to `results/metrics.csv`;
- regenerate or update `results/RESULTS.md` using the existing project mechanism;
- perform mechanical consistency, correctness, provenance, and repeatability checks;
- make only the repository changes required to execute and document this task;
- use bounded Track-1 operational retries allowed by the existing workflow when an attempt fails for a clearly operational reason, while preserving every failed attempt.

Any affinity controls selected for the controlled runs must be explicitly documented and held constant across repetitions of a given configuration.

#### Prohibited

Codex and workers must not:

- rebuild LULESH;
- change source code;
- change compiler environment;
- change compiler optimization flags;
- test `-O2`, `-Ofast`, or other compiler settings;
- test additional OpenMP thread counts such as 2, 4, 16, or 32;
- perform an OpenMP scaling sweep;
- change the MPI rank count from 1;
- perform MPI scaling;
- change the `-s 30` workload;
- investigate fixed-global-size MPI strong scaling;
- begin a broader NUMA optimization campaign;
- install packages;
- use `sudo`;
- change shared software;
- modify authentication configuration;
- promote the 8-thread configuration to baseline;
- update strategic conclusions in `planning/analysis/`;
- perform campaign-level causal interpretation;
- recommend or start the next optimization direction;
- expand the task beyond the controlled 1-thread versus 8-thread validation.

### 1.7 Execution Constraints

Use the existing CCE13/O3 binary and the existing source revision.

The primary controlled comparison is:

```text
Configuration A
MPI ranks:       1
OpenMP threads:  1
Problem:         -s 30

Configuration B
MPI ranks:       1
OpenMP threads:  8
Problem:         -s 30
```

Where operationally valid, both configurations should request the same PBS resource envelope:

```text
select=1:ncpus=8:mpiprocs=1:mem=16gb
```

The intent is to hold scheduler allocation broadly constant while changing OpenMP parallelism.

Affinity must be **verified**, not inferred merely from requested resources or absence/presence of a warning.

For the 8-thread case, evidence must show whether the eight OpenMP threads occupy distinct allocated CPU resources.

For the 1-thread case, record the corresponding placement of the single OpenMP thread.

Do not suppress or discard affinity warnings. Preserve them as evidence even when explicit placement diagnostics show a valid layout.

Use normal Aspire2A rules:

- persistent SSH connection check;
- non-interactive `BatchMode=yes`;
- project-root filesystem scope;
- PBS-only compute execution;
- no computation on login nodes;
- bounded scheduler polling;
- existing Git synchronization and push authorization rules.

### 1.8 Success Criteria

Execution is complete when:

1. the exact existing CCE13/O3 binary and source revision have been verified;
2. the controlled affinity mechanism and diagnostic method have been recorded;
3. three 1-thread attempts and three 8-thread attempts have been executed, unless a defined stop condition is triggered;
4. actual thread-placement evidence is preserved for the controlled configurations;
5. every completed attempt has its raw stdout/stderr preserved;
6. every completed attempt has provenance and requested-resource metadata;
7. every completed attempt has its elapsed time, FOM, and correctness fields extracted;
8. each repetition is represented separately in `results/metrics.csv`;
9. scientific correctness has been operationally checked for every completed run;
10. Codex verifies that evidence paths, run IDs, units, and result rows are internally consistent;
11. the Codex Execution Report identifies all completed, failed, retried, missing, or blocked attempts;
12. execution remains within the approved scope.

These criteria establish an analyzable dataset. They do **not** prove that either configuration is strategically preferable.

### 1.9 Stop / Escalation Conditions

Stop the affected workflow and report rather than silently widening scope if:

- the existing CCE13/O3 binary is missing or differs from the expected revision/configuration;
- valid thread placement cannot be established within the authorized PBS resource envelope and ordinary OpenMP/Cray runtime controls;
- establishing valid affinity would require changing scheduler policy, launcher strategy, MPI rank count, source code, compiler flags, or shared system configuration;
- thread-placement diagnostics show unintended oversubscription that cannot be corrected within the approved scope;
- any controlled run produces failed or non-finite scientific correctness;
- correctness becomes ambiguous;
- the result schema would require a semantic/schema change rather than compatible row appends;
- repository or cluster synchronization becomes ambiguous;
- execution requires package installation, `sudo`, deletion, or access outside the approved project root;
- a new scientific experiment or broader optimization direction appears necessary;
- required evidence cannot be obtained within scope.

Preserve all evidence collected before stopping.

### 1.10 Strategic Analyst Notes

This task intentionally compares only **1 thread versus 8 threads**.

Do not expand it into a 1/2/4/8/16/32 OpenMP sweep even if such a sweep appears useful.

The main purpose is to determine whether the current 8-thread candidate is trustworthy enough to justify subsequent optimization work.

Affinity diagnostics are evidence. Absence of the original Cray warning is not, by itself, proof that placement is correct.

Prefer a controlled and reproducible experiment over trying additional tuning variables.

### 1.11 Authorization

status: APPROVED

approved_scope: Controlled affinity and repeatability validation of the existing CCE13/O3 LULESH `-s 30` binary: three 1-MPI × 1-OpenMP attempts and three 1-MPI × 8-OpenMP attempts under a comparable 8-CPU PBS allocation, with verified thread placement, correctness/provenance capture, compatible result updates, and no broader optimization, rebuild, source/compiler/workload/MPI-rank changes.

approved_by: user

---

## 2. CODEX EXECUTION REPORT

### 2.1 Execution Status

status: <COMPLETE | PARTIAL | BLOCKED | FAILED>

### 2.2 Orchestration Summary

*Workers, responsibilities, dependencies, and follow-ups.*

### 2.3 Work Executed

*Factual work performed.*

### 2.4 Operational Validation

*Evidence, correctness, provenance, consistency, and scope checks.*

### 2.5 Evidence and Artifacts

*Reference raw evidence paths and revisions; do not duplicate outputs.*

### 2.6 Files Changed

*List files or state None.*

### 2.7 Missing / Unavailable Evidence

*List gaps or state None.*

### 2.8 Execution Errors / Exceptions

*List failures and exceptions or state None.*

### 2.9 Scope Compliance

*State whether work stayed within the approved scope.*

### 2.10 Handoff to Strategic Analyst

*Give factual reading guidance, without strategic interpretation.*
