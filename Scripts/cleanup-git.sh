#!/bin/bash
# CircleCI isn't smart about branches, so we should make double sure there are no release objects
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch Monoid*.zip' --prune-empty --tag-name-filter cat -- --all
rm -rf .git/refs/original
git reflog expire --expire=now --all
git gc --force --prune=now
exit 0 # Because sometimes git is silly and throws 129 even on force
