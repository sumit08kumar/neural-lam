# Contributing

## Development Setup

1. Clone the repository
2. Install with development dependencies:
   ```bash
   uv pip install --group dev -e .
   ```

## Pre-commit Hooks

```bash
pre-commit run --all-files
```

## Running Tests

```bash
pytest -vv -s --doctest-modules
```

## Building Documentation Locally

```bash
pip install jupyter-book sphinx-autoapi myst-nb sphinx-copybutton pydata-sphinx-theme
jupyter-book build docs/
```

The built documentation will be in `docs/_build/html/`.

## Pull Requests

Please use the [PR template](https://github.com/mllam/neural-lam/blob/main/.github/pull_request_template.md).

## Contact

Join the [mllam Slack channel](https://join.slack.com/t/ml-lam/shared_invite/zt-2t112zvm8-Vt6aBvhX7nYa6Kbj_LkCBQ)
or open a [GitHub issue](https://github.com/mllam/neural-lam/issues).
