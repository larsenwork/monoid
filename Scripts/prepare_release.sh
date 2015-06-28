#!/bin/bash
shopt -s extglob
git rm -f ./*.zip || echo "No releases"
cd _release
for f in Monoid-Regular*.ttf; do
    # Get the built options
    options=${f#Monoid-Regular}
    echo "Options: ${options}"
    # Add all the fonts with those options
    zip -j "../Monoid${options%.ttf}.zip" Monoid-+([^-])$options
done
cd ..
#sudo rm -rf _release
