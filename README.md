# Python Interview Questions (100)

This repo contains 100 Python interview questions with:
- Problem statements
- My implementations
- Optimized solutions
- Tests
- Notes

## Structure
- questions/ → practice
- solutions/ → reference answers
- tests/ → validation
- notes/ → learning insights

## Running tests

Run tests from the project root:

```bash
venv/bin/pytest -q
```

If your virtual environment is already activated, this also works:

```bash
pytest -q
```

To run a subset of tests, use `-k`:

```bash
venv/bin/pytest -k palindrome
```

If you are inside the `questions/` folder, either go back to the project root first:

```bash
cd ..
venv/bin/pytest -q
```

or run pytest with the parent-relative path:

```bash
../venv/bin/pytest -q
```
