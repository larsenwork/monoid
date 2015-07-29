#!/usr/bin/env python2.7
# vim: sts=4 sw=4 ts=4 et

import sys
if len(sys.argv) < 4:
    usage = """Build should be run with 3 arguments:

    First: The total possible number of parallel processes (1+)
    Second: The parallel batch number (0+)
    Third: The .sfdir for the font
    """
    print >> sys.stderr, usage
    exit(1)

from fontbuilder import *

# Output directory
output = "_release"

# Options to generate
conflicting(
    style('Loose', Bearing(right=128)),
    style('HalfLoose', Bearing(right=64)),
#   style('normal', Bearing(left=0)),
    style('HalfTight', Bearing(left=-64)),
    style('Tight', Bearing(left=-128))
)

conflicting(
    option('XtraSmall', '13px', Line(1536, 256)),
    option('Small', '14px', Line(1536, 384)),
#   option('medium', 15px', Line(1664, 384)),
    option('Large', '16px', Line(1664, 512)),
    option('XtraLarge', '17px', Line(1792, 512))
)

# ss01
option('Dollar', 'Alt $', Swap("dollar", "dollar.empty"))
# ss03
option('0', 'Alt 0', Swap("zero", "zero.dot"))
# ss05
option('1', 'Alt 1', Swap("one", "one.base"))
# ss08
option('l', 'Alt l', Swap("l", "l.zstyle"))
# ss14
# option('Squeeze', 'Squeezed capitals with diacritics', SwapLookup("ss14"))
# no calt
option('NoCalt', 'Turn off contextual alternates', DropCAltAndLiga())

# Build options in
build_batch(output, sys.argv[3], int(sys.argv[1]), int(sys.argv[2]))
