# Trackle

Trackle is a lightweight, local-first, git-aware ML experiment tracker.

## Goals

- Local filesystem storage only
- No servers or networking
- Simple Python API and CLI
- Git-based reproducibility

## Quick start

```bash
pip install -e .
```

```python
import trackle

trackle.init(run_name="demo")
trackle.log_params({"lr": 0.01})
trackle.log_metric("loss", 0.5, step=1)
trackle.finish()
```

