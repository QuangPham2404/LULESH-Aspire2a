# Tasks

Each bounded strategic action uses one numbered task file, such as
`TASK-001.md`. The task is the execution contract between the Strategic
Analyst, Human Leader, and Codex. Codex works only on the exact task identified
by the user and only after it is approved.

## Create and approve a task

1. Copy `TASK-TEMPLATE.md` to the next unused `TASK-XXX.md` filename.
2. Have the Strategic Analyst complete the `STRATEGIC SPECIFICATION` and
   identify the allowed scope, required evidence, success criteria, and stop
   conditions.
3. The Human Leader reviews and approves the specification. An executable
   task records `status: APPROVED`, `current_owner: codex`, and
   `approved_by: user` in its front matter.
4. Identify the exact approved task file when asking Codex to execute it.
5. Codex appends the `CODEX EXECUTION REPORT` to that same task file.

The template is a drafting aid, not an active task or authorization. Do not
execute a task with `status: DRAFT` or infer the active task from file dates.
Keep raw benchmark and probe evidence in its canonical output locations and
reference it from the task.
