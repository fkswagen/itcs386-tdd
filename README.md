# itcs386-tdd

TDD lab for ITCS386: Python unit testing with pytest and Test-Driven Development.

## Running tests

Run these commands from the repository folder with the virtual environment activated.

```powershell
python -m pytest -q
```

## Step 0.7: Running tests selectively

Practiced the following pytest options:

| Command | Purpose |
| --- | --- |
| `python -m pytest -q` | Show concise test results. |
| `python -m pytest -v` | Show each test's name and result. |
| `python -m pytest -x` | Stop at the first failure. |
| `python -m pytest -k leap` | Run tests matching `leap`. |
| `python -m pytest --lf` | Rerun previously failed tests; run all tests if no failures are recorded. |
