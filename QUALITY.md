# Quality Checks

### Running the Checks

To run the code quality checks, run the following command:

```bash
flake8
```

### Fixing Code Quality Issues

- If you have `isort` installed, you can run `isort .` to automatically fix import order issues.
    - `flake8` will report `isort` related issues as `I` errors.
- You may fix other issues manually.