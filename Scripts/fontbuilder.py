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

def _build(dstdir, font, permutations):
    # Ensure that the destination directory exists
    try:
        mkdir(dstdir)
    except OSError:
        pass

    for prcnt, opts in permutations:
        # Open the original font
        fnt = fontforge.open(font)

        # Get the base name for the font
        name = join(dstdir, fnt.fontname)

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

        # Log progress to prevent timeoout
        print(str(prcnt) + '%.. ' + name)

def build(dstdir, font):
    _build(dstdir, font, permutations())

def build_batch(dstdir, font, total_nodes, node_number):
    # Starting at (i) node_number, build option every (n) total_nodes
    _build(dstdir, font, list(permutations())[node_number::total_nodes])

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

def Swap(glyph1, glyph2):
    """Swaps the places of two glyphs"""
    def swap_op(fnt):
        # Unlike selections, glyph layer data is returned as a copy
        swp = fnt[glyph1].foreground
        fnt[glyph1].foreground = fnt[glyph2].foreground
        fnt[glyph2].foreground = swp
    return swap_op

def SwapLookup(lookup):
    """Swaps the places of glyphs based on an OpenType lookup table"""
    def swaplookup_op(fnt):
        # Get every subtable for every matching lookup
        lookups = [i for i in fnt.gsub_lookups if fnt.getLookupInfo(i)[2][0][0] == lookup]
        subtables = []
        for lookup in lookups:
            for subtable in f.getLookupSubtables(lookup):
                subtables.append(subtable)

        for glyph in fnt.glyphs():
            subbed = False

            for subtable in subtables:
                posSub = glyph.getPosSub(subtable)
                if not subbed and posSub and posSub[0][1] == "Substitution":
                    subbed = True # Don't double tap if there are duplicates

                    sub = posSub[0][2]
                    swp = glyph.foreground
                    glyph.foreground = fnt[sub].foreground
                    fnt[sub].foreground = swp

    return swaplookup_op

def DropCAltAndLiga():
    """Removes Contextual Alternates and Ligatures"""
    def dropcaltandliga_op(fnt):
        for lookup in fnt.gsub_lookups:
            if fnt.getLookupInfo(lookup)[0] in ['gsub_ligature', 'gsub_contextchain']:
                fnt.removeLookup(lookup)

    return dropcaltandliga_op

def Variation(name):
    """Changes the subfamily/variation of the font"""
    def variation_op(fnt):
        # Get the SFNT information as dictionary {property: value}
        # where English (US) is the language... Here be dragons.
        #
        #                                      o
        #                                     /\
        #                                    /::\
        #                                   /::::\
        #                     ,a_a         /\::::/\
        #                    {/ ''\_      /\ \::/\ \
        #                    {\ ,_oo)    /\ \ \/\ \ \
        #                    {/  (_^____/  \ \ \ \ \ \
        #          .=.      {/ \___)))*)    \ \ \ \ \/
        #         (.=.`\   {/   /=;  ~/      \ \ \ \/
        #             \ `\{/(   \/\  /        \ \ \/
        #              \  `. `\  ) )           \ \/
        #               \    // /_/_            \/
        #                '==''---))))
        sfnt_dict = {sfnt[1]: sfnt[2] for sfnt in fnt.sfnt_names if sfnt[0] == 'English (US)'}

        fnt.familyname = sfnt_dict['Family'] + ' ' + name
        fnt.fullname = fnt.familyname + ' ' + sfnt_dict['SubFamily']
        fnt.fontname = fnt.fullname.replace(' ', '-')

        fnt.appendSFNTName('English (US)', 'Family', fnt.familyname)
        fnt.appendSFNTName('English (US)', 'Fullname', fnt.fullname)
        fnt.appendSFNTName('English (US)', 'PostScriptName', fnt.fontname)
        fnt.appendSFNTName('English (US)', 'SubFamily', sfnt_dict['SubFamily'])
        fnt.appendSFNTName('English (US)', 'UniqueID', sfnt_dict['UniqueID'] + ' : ' + name)
    return variation_op
