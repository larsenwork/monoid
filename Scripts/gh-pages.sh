#!/bin/bash
git checkout gh-pages

# Ensure release byproducts are not included
git branch -D release
[[ -e _release ]] && git rm -rf _release

# Convert to webfonts
./node_modules/.bin/ttf2eot /tmp/monoid-normal.ttf /tmp/monoid-normal.eot
./node_modules/.bin/ttf2woff /tmp/monoid-normal.ttf /tmp/monoid-normal.woff
./woff/woff2_compress /tmp/monoid_normal.ttf

cp /tmp/monoid-normal.* css/
git add css
git commit -m "Update web fonts for ${CIRCLE_SHA1}"
git push origin gh-pages
