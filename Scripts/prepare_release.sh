#!/bin/bash
shopt -s extglob
for f in ./Monoid-Regular*.ttf; do
    # Get the built options
    options=${f#Monoid-Regular}
    # Add all the fonts with those options
    zip -j "../Monoid${options%.ttf}.zip" Monoid-+([^-])$options
done
