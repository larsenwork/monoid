#!/usr/bin/env python2.7
# vim: sts=4 sw=4 ts=4 et

from fontbuilder import *

# Configuration
## Source directory
source = "Source"

## Output directory
output = "_release"

## Fonts to modify
## To be added when the script supports it + the fonts are done 'Monoid-Oblique.sfdir', 'Monoid-Bold.sfdir'
fonts = ['Monoid.sfdir']

# Options to generate
conflicting(
    style('loose', Bearing(right=128)),
    style('halfloose', Bearing(right=64)),
#   style('normal', Bearing(left=0)),
    style('halftight', Bearing(left=-64)),
    style('tight', Bearing(left=-128))
)

conflicting(
    option('xtrasmall', '13px', Line(1536, 128)),
    option('small', '14px', Line(1536, 256)),
#   option('medium', 15px', Line(1664, 256)),
    option('large', '16px', Line(1664, 384)),
    option('xtralarge', '17px', Line(1792, 384))
)

option('1', 'Alt 1', Swap("one", "one.base"))
option('3', 'Alt 3', Swap("three", "three.russian"))
option('l', 'Alt l', Swap("l", "l.zstyle"))
option('s', 'Alt s', Swap("s", "s.retina"))
option('dollar', 'Alt $', Swap("dollar", "dollar.empty"))
option('asterisk', 'Alt asterisk', Swap("asterisk", "asterisk.multi"))

for font in fonts:
    build(output, source, font)
