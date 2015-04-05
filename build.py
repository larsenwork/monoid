#!/usr/bin/env python2.7
# vim: sts=4 sw=4 ts=4 et

from fontbuilder import *

# Configuration
## Source directory
source = "Source"

## Output directory
output = "_release"

## Fonts to modify
fonts = ['Monoid.sfdir']

# Options to generate
conflicting(
    style('Loose', Bearing(right=128)),
    style('HalfLoose', Bearing(right=64)),
    style('HalfTight', Bearing(left=-64)),
    style('Tight', Bearing(left=-128)),
)

option('al', 'Alternative l', Swap("l", "l.alt"))
option('a1', 'Alternative 1', Swap("one", "one.alt"))
option('sa', 'Standard asterisk', Swap("asterisk", "asterisk.alt"))

conflicting(
    option('17px', 'Deci', Line(ascent=1664, descent=512)),
    option('19px', 'Deca', Line(1792, 512)),
    option('20px', 'Hecto', Line(1792, 640)),
)

conflicting(
    option('sz', 'Slashed zero', Swap("zero", "zero.slashed")),
    option('uz', 'Undotted zero', Swap("zero", "zero.dotless")),
)

for font in fonts:
    build(output, source, font)
