# `scripts/`

General reusable helper scripts live here.

Use this directory for automation that does not naturally belong to a more
specific directory, such as:

- checking that local and Aspire2A clones are on the expected branch/commit
- checking remote project state
- validating repository structure
- shared workflow utilities

Scripts specific to builds should live under `builds/`. Scripts specific to
result extraction or plotting should live under `results/scripts/`. Run scripts
should live under the relevant `experiments/<run_name>/` directory.

Avoid full-tree sync scripts unless there is a specific need. The normal model
is that both the local PC and Aspire2A have real Git clones, with Git used to
move tracked workflow files between environments.
