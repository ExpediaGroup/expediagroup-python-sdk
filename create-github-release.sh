#!/bin/bash

release_notes=$1
echo "$release_notes" &> release-notes.txt
sed -i '1d' release-notes.txt

previous_tag=$(./get-latest-tag.sh)
today="v$(date "+%Y%m%d")"

echo "today: $today"

git tag "$today"
git push --tags
gh release create "$today" --draft --generate-notes --latest --notes-file release-notes.txt --notes-start-tag "$previous_tag" --title "$today"
