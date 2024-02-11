#!/bin/bash

tags=("v1.0.0" "v1.0.1" "v1.1.0" "v2.0.0")

for tag in "${tags[@]}"; do
    if [ $(git tag -l "$tag") ]; then
        git push origin --delete "$tag"
        echo "Deleted $tag"
    fi
done
