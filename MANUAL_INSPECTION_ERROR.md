# Manual Inspection Errors

## Case TASK-001-OMP-AFFINITY-001

- **Status:** `USER_ACTION_REQUIRED`
- **Created:** 2026-09-26
- **Task:** `TASK-001` — Controlled OpenMP Affinity and Repeatability Validation
- **Affected workflow:** `experiments/cce13-craympich8-s30-affinity-repeatability/`
- **Error class:** Cray OpenMP thread affinity binding / placement failure

### Observed facts

- Both attempts used the existing CCE 13.0.2 / Cray MPICH 8.1.15 binary,
  source revision `3e01c40b3281aadb7f996525cdd4a3354f6d3801`, and the approved
  PBS request `select=1:ncpus=8:mpiprocs=1:mem=16gb`.
- Attempt `CCE13-CrayMPICH8-s30-affinity-omp1_v1`, PBS job
  `25556314.pbs101`, ran on `x1001c2s2b0n1`. Its stdout records one OpenMP
  thread with `affinity: 0`; stderr contains one
  `[CCE OMP] affinity unbinding error: Invalid argument` message.
- Attempt `CCE13-CrayMPICH8-s30-affinity-omp8_v1`, PBS job
  `25556332.pbs101`, ran on `x1001c2s5b1n0`. Its stdout records threads 0–7
  all with `affinity: 0`; stderr contains the Cray oversubscription warning
  and eight `[CCE OMP] affinity unbinding error: Invalid argument` messages.
- Both jobs ended in PBS state `F` with exit status 0. Both emitted
  `Run completed:` and finite correctness values. These facts do not establish
  valid distinct placement for the 8-thread case.
- Raw evidence is preserved locally and on Aspire2A:
  - `experiments/cce13-craympich8-s30-affinity-repeatability/outputs/CCE13-CrayMPICH8-s30-affinity-omp1_v1.o`
  - `experiments/cce13-craympich8-s30-affinity-repeatability/outputs/CCE13-CrayMPICH8-s30-affinity-omp1_v1.e`
  - `experiments/cce13-craympich8-s30-affinity-repeatability/outputs/CCE13-CrayMPICH8-s30-affinity-omp8_v1.o`
  - `experiments/cce13-craympich8-s30-affinity-repeatability/outputs/CCE13-CrayMPICH8-s30-affinity-omp8_v1.e`

### Suspected causes and unresolved questions

- The runtime did not establish distinct per-thread affinity under the
  requested allocation and selected OpenMP controls. The affinity report and
  unbinding errors do not identify why binding failed.
- It remains unresolved whether the cause is the runtime’s interpretation of
  the PBS CPU set, a site-level affinity interaction, or another CCE/runtime
  condition. No cause has been confirmed.
- No remediation has been tested or authorized.

### Stop and required decision

- Attempts 3–6 were not submitted. No retry, affinity change, launcher change,
  scheduler-policy change, or shared-system change was made.
- The affected workflow is stopped under Task-001 §1.9. Review this case and
  explicitly decide whether to authorize a narrowly scoped diagnostic or
  affinity-control retry, request another operational investigation, or leave
  Task-001 blocked. Any changed settings require new attempt names and output
  paths; preserve both existing attempts.

### Resolution record

- Pending Human Leader decision.
