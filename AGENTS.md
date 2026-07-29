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
- Commit rules: only commit the scripts/results/etc when the build/run is SUCCESFULL. For unsuccessful cases, record the errors, your corresponding implemented solution clearly as you try to patch the errors yourself. The agent have permission to self patch build/run errors yourself unless specified otherwise.
- Manage the local PC clone and Aspire2A clone with this procedure:
  - Before starting work in either environment, run `git status` and `git pull --ff-only`.
  - Before committing, run `git status` and inspect the relevant diff.
  - Commit only reviewed/useful scripts, plans, progress notes, extracted results, metadata, and logs.
  - Prefer committing and pushing from the local PC.
  - After pushing from one environment, pull with `git pull --ff-only` in the other environment before continuing work there.
  - If `git pull --ff-only` fails because the clones diverged, stop and inspect instead of creating a merge commit.
- Prefer local Git operations.
- Do not store GitHub credentials on Aspire2A.
- Do not push without explicit user approval.
- Do not commit raw temporary files unless requested.

# Section start-up action

At the start of every session, read the latest progress report in ```/progress``` to get the context on what is completed and what we are doing next.
