# Contributing to django-mui

Thanks for contributing.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt ruff
```

## Local QA checks

Run the same checks as CI before opening or updating a pull request:

```bash
ruff check .
ruff check . --select S
python -m unittest discover -s tests -p "test_*.py"
```

## Contribution workflow

1. Create a branch for your change.
2. Keep changes focused and minimal.
3. Run the local QA checks.
4. Open a pull request with a clear description of scope and validation.
