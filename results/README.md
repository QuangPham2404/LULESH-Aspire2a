# `results/`

This directory contains structured result files extracted from raw output in
`experiments/`.

Use whatever layout fits the project, but keep extracted results separate from
raw `.o` and `.e` files.

Example:

```text
results/
├── metrics.csv
├── metadata.json
└── scripts/
```

- `metadata.json`: run metadata needed for reproducibility and auditing.
- `metrics.csv`: parsed numerical results for comparison and plotting.
- `scripts/`: extraction, parsing, or plotting scripts specific to results.

Do not rely on exit code alone. Record whether the expected LULESH output was
produced and whether the result passed the chosen correctness criteria. Planning
and interpretation belong in `planning/`.
