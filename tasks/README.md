# Tasks

Each bounded strategic action uses one numbered task file, such as
`TASK-001.md`. The task is the execution contract between the Strategic
Analyst, Human Leader, and Codex. Codex works only on the exact synchronized
task identified by the user and only after it is approved.

## Create and approve a task

1. Draft the task from the canonical template at
   `workflow/TASK-TEMPLATE.md`; retain its front matter and both numbered
   sections.
2. The Strategic Analyst completes the `STRATEGIC SPECIFICATION`, including
   the bounded scope, required evidence, success criteria, stop conditions,
   and `1.11 Authorization` fields.
3. The Human Leader reviews and explicitly approves the task. Set front matter
   to `status: APPROVED` and `current_owner: codex`, and record
   `status: APPROVED`, the exact `approved_scope`, and `approved_by: user` in
   `1.11 Authorization`.
4. Materialize the approved content in the repository and synchronize it
   before identifying the exact task for execution.
5. Codex completes the `CODEX EXECUTION REPORT` in that same task file.

`TASK-TEMPLATE.md` in this directory is retained as a legacy pointer; it is
not a task template. Do not execute a draft or infer the active task from file
dates. Keep raw benchmark and probe evidence in canonical output locations and
reference it from the task.
