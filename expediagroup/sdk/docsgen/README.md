# Expedia Group Documentation Generator for Python

The Expedia Group Documentation Generator for Python generates markdown for Python 3 packages.

## Usage
To generate markdown documentation for your code, follow the steps below.
1. Install dependencies using the command ``pip install -r requirements-docs.txt``
2. ``cd`` to `expediagroup/sdk/docsgen` directory.
3. Run the ``__main__.py`` script.
```shell
python3 ./__main__.py -p [PACKAGE DIR]  -n [PACKAGE NAME] -t [OPTIONAL CUSTOM TEMPLATES DIR] -o [OPTIONAL OUTPUT DIR]
```
4. Use [mdformat](https://mdformat.readthedocs.io/en/stable/users/installation_and_usage.html) optionally to format the final output.

## Contributing

Please refer to [CONTRIBUTING](CONTRIBUTING.md) for details.

## License

This project is licensed under the Apache License v2.0 - see the [LICENSE](LICENSE) for details.
