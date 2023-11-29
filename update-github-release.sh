#!/bin/bash

nextVersion=$1
today=$(date "+%Y%m%d")
git tag v"$today" "$nextVersion"
git push --tags
gh release edit "$nextVersion" --title v"$today" --tag v"$today"
