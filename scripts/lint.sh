#!/bin/sh

cd ..
pip3 install -r requirements-dev.txt

isort .
black .
docformatter --recursive --black --in-place --close-quotes-on-newline --config ./pyproject.toml .
echo ""
