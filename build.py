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
    style('loose', Bearing(right=128)),
    style('halfloose', Bearing(right=64)),
#   style('normal', Bearing(left=0)),
    style('halftight', Bearing(left=-64)),
    style('tight', Bearing(left=-128)),
)

conflicting(
    option('xsmall', '14px', Line(ascent=1408, descent=384)),
    option('small', '15px', Line(1408, 512)),
#   option('medium', '16px', Line(1536, 512)),
    option('large', '17px', Line(1536, 640)),
    option('xlarge', '18px', Line(1792, 640)),
)

option('a0', 'Alt 0', Swap("zero", "zero.alt"))
option('a1', 'Alt 1', Swap("one", "one.alt"))
option('a3', 'Alt 3', Swap("three", "three.alt"))
option('al', 'Alt l', Swap("l", "l.alt"))
option('ad', 'Alt $', Swap("dollar", "dollar.alt"))
option('aa', 'Alt asterisk', Swap("asterisk", "asterisk.alt"))


for font in fonts:
    build(output, source, font)
