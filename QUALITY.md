# Quality Checks

### Running the Checks

To run the code quality checks, run the following command:

```bash
flake8 expediagroup/ generator/
```

### Fixing Code Quality Issues

- You can run `isort expediagroup/ generator/` to automatically fix import order issues.
    - `flake8` will report `isort` related issues as `I` errors.
- You can run `black expediagroup/ generator/` to automatically fix formatting issues.
    - `flake8` will report `black` related issues as `BLK` errors.
- You may fix other issues manually.
