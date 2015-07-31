#!/bin/bash
shopt -s extglob

# Copy artifacts to keep after branch switch
cp Scripts/gh-pages.sh /tmp
cp Source/Readme+License.html /tmp
cp Monoisome/Monoisome-Regular.ttf /tmp

# Switch to release branch
git checkout release

cd _release
for f in Monoid-Regular*.ttf; do
    # Get the built options
    options=${f#Monoid-Regular}
    echo "Options: ${options}"
    # Add all the fonts with those options
    zip -j "../Monoid${options%.ttf}.zip" Monoid-+([^-])$options /tmp/Readme+License.html tmp/Monoisome-Regular.ttf
done
cd ..
sudo rm -rf _release
