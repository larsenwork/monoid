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

# ss01
option('dollar', 'Alt $', Swap("dollar", "dollar.empty"))
# ss02
option('asterisk', 'Alt asterisk', Swap("asterisk", "asterisk.multi"))
# ss03
option('0', 'Alt 0', Swap("zero", "zero.dot"))
# ss05
option('1', 'Alt 1', Swap("one", "one.base"))
# ss06
option('3', 'Alt 3', Swap("three", "three.russian"))
# ss08
option('l', 'Alt l', Swap("l", "l.zstyle"))

# Build options in 
build_batch(output, sys.argv[3], int(sys.argv[1]), int(sys.argv[2]))
