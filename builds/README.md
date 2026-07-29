# `builds/`

This directory contains build-related material for LULESH variants.

Suggested layout:

```text
builds/
├── source/
├── build-scripts/
└── extra-packages/
```

- `source/`: source code cloned or copied for building the application with
  different compilation methods.
- `build-scripts/`: reusable build scripts kept for record and handoff.
- `extra-packages/`: explicitly approved local dependencies or vendored
  packages, if needed.

Do not install or modify shared software on Aspire2A. Prefer available modules.
Ask for user approval before adding a new package that is not already available.
