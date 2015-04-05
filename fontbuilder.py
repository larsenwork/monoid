# Copyright 2015 Chase Colman (chase@colman.io)
# LICENSE: MIT
# vim: sts=4 sw=4 ts=4 et

import fontforge
from itertools import compress
from os import mkdir
from os.path import basename, splitext, join

# Builder
def style(name, does):
    if not isinstance(does, list):
        does = [does]
    option(name, name, [Variation(name)] + does)

    return name

def option(abrv, name, does):
    if not isinstance(does, list):
        does = [does]
    option.operations[abrv] = does
    option.abrvs.append(abrv)
    option.names[abrv] = name

    return abrv

# Initialize the operations map, abbreviation list, and name map
option.operations = {}
option.abrvs = []
option.names = {}

def conflicting(*abrvs):
    """Wrap the abbreviations as a tuple in the option abbreviation list"""
    # Assumes last #abrvs abbreviations are conflicting options
    option.abrvs = option.abrvs[:-len(abrvs)] + [tuple(abrvs)]

def _expand_options(bitmap):
    # Apply the bitmap to the options
    opts = compress(option.abrvs, bitmap)

    # Expand the permutations for all options
    expanded = [[]]
    for opt in opts:
        if isinstance(opt, tuple):
            expanded = [items + [prmtn] for items in expanded for prmtn in opt]
        else:
            expanded = [items + [opt] for items in expanded]

    return expanded

def permutations():
    """Yields all possible permutations from the options list"""
    count = len(option.abrvs)

    # Each option is a binary choice, so we use an int as a quick bitmap.
    # To iterate over every possible permutation, all we have to do is increment
    # up to the maximum value 2^(#options)
    bitmap_max = 1 << count

    # Iterate over all possible permutations
    for i in xrange(bitmap_max):
        # Map the iteration's permutations using a bitmap
        bitmap = [i >> n & 1 for n in xrange(count)]
        for opts in _expand_options(bitmap):
            yield(int(float(i)/bitmap_max*100), opts)

def build(dstdir, srcdir, font):
    # Ensure that the destination directory exists
    try:
        mkdir(dstdir)
    except OSError:
        pass

    for prcnt, opts in permutations():
        # Open the original font
        fnt = fontforge.open(join(srcdir, font))

        # Get the base name for the font
        base = fnt.fontname.split('-')[0]
        name = join(dstdir, base)

        for opt in opts:
            # Append this option to the font name
            name += '-' + str(opt)
            # Run all the operations for this option
            for oper in option.operations[opt]:
                oper(fnt)

        # Add the extension
        name += ".ttf"

        # Output the file and cleanup
        fnt.generate(name)
        fnt.close()

        # Log progress to prevent Wercker from timing out
        print(str(prcnt) + '%.. ' + name)

# Operations
## NOTE:
## All operations return a closure with the 1st argument being a fontforge.font
def Line(ascent, descent):
    """Sets the ascent and/or descent of the font's line"""
    def line_op(fnt):
        fnt.os2_winascent = fnt.os2_typoascent = fnt.hhea_ascent = ascent
        fnt.os2_windescent = descent
        fnt.os2_typodescent = fnt.hhea_descent = -descent
    return line_op

def Bearing(left=0, right=0):
    """Adjusts the left and/or right bearings of all glyphs"""
    def bearing_op(fnt):
        for glyph in fnt.glyphs():
            if left != 0:
                glyph.left_side_bearing += left
            if right != 0:
                glyph.right_side_bearing += right
    return bearing_op

DEL = 127
def Swap(glyph1, glyph2):
    """Swaps the places of two glyphs using the DEL char as swap space"""
    def swap_op(fnt):
        # Unlike selections, glyph layer data is returned as a copy
        swp = fnt[glyph1].foreground
        fnt[glyph1].foreground = fnt[glyph2].foreground
        fnt[glyph2].foreground = swp
    return swap_op

def Variation(name):
    """Changes the subfamily/variation of the font"""
    def variation_op(fnt):
        base = fnt.fontname.split('-')[0]
        fontname = [base] + name.split()
        fnt.fontname = '-'.join(fontname)
        fnt.fullname = ' '.join(fontname)
    return variation_op
