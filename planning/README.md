# `planning/`

This directory contains the optimization master tracker and detailed result
analysis.

Use this directory for:

- optimization ideas
- experiment hypotheses
- planned commands and resource requests
- result summaries
- interpretation of wins, regressions, failures, and noise
- decisions about next experiments

`PLANS.md` is the concise master tracker with three sections: the current
baseline, an optimization-direction table that also serves as analysis
history, and the agreed next direction. Detailed analyses are stored in
`planning/analysis/`, one stable `<analysis-id>.md` file per optimization
direction or independently grouped question. Each analysis presents selected
data from `results/metrics.csv`, interprets the results, records limitations,
and suggests a next section for user review.

Analysis is started manually with the `ANALYSE_RESULTS` command. The command
does not authorize job submission, workflow changes, or automatic application
of optimization decisions. `results/metrics.csv` remains the structured source
of truth; analysis files are documented interpretations with provenance.
