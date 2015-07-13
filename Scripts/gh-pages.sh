#!/bin/bash
git checkout gh-pages

# Ensure release byproducts are not included
git branch -D release
[[ -e _release ]] && git rm -rf _release

# Convert to webfonts
for f in /tmp/*.ttf; do
nosuffix=${f%.ttf}
./node_modules/.bin/ttf2eot $f $nosuffix.eot
./node_modules/.bin/ttf2woff $f $nosuffix.woff
./woff2/woff2_compress $f
done

cp /tmp/*.{eot,woff,woff2,ttf} css/
git add css
git commit -m "Update web fonts for ${CIRCLE_SHA1} [ci skip]"
git push origin gh-pages
