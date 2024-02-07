#!/bin/bash

git fetch --tags
tags=$(git tag -l "v*")
latest_tag=$(echo "$tags" | grep -E '^v[0-9]+$' | sort -Vr | head -n 1)

echo "$latest_tag"
