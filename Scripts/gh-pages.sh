#!/bin/bash

# Convert to webfonts
for f in /tmp/*.ttf; do
nosuffix=${f%.ttf}
./node_modules/.bin/ttf2eot $f $nosuffix.eot
./node_modules/.bin/ttf2woff $f $nosuffix.woff
./woff2/woff2_compress $f
done

git show --format="window.MONOID_URL = 'https://cdn.rawgit.com/larsenwork/monoid/%H/'" -s release > /tmp/release.js

git fetch -f -p origin gh-pages:gh-pages
git checkout gh-pages

# Ensure release byproducts are not included
git branch -D release
[[ -e _release ]] && git rm -rf _release

cp /tmp/*.{eot,woff,woff2,ttf} css/
cp /tmp/release.js js/
git add css
git add js
git commit -m "Update web fonts for ${CIRCLE_SHA1} [ci skip]"
git pull --rebase origin gh-pages
git push origin gh-pages
