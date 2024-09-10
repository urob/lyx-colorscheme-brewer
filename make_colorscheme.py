#!/usr/bin/python3
"""
Colorscheme brewer for LyX

Usage: ./make_colorscheme.py palette
Output: out/palette_lyx_cs
"""

import os
import sys

# get color palette from commmand line argument
colors = str(sys.argv[1])

# import color definitions
sys.path.append('./colors')
palette = __import__(colors).palette

# map the palette to LyX colors
# https://www.lyx.org/trac/browser/lyxgit/src/Color.cpp
# https://www.lyx.org/trac/browser/lyxgit/src/ColorCode.h
colorscheme = {
    # The different text colors
    'black':                     palette['black'],
    'white':                     palette['white'],
    'blue':                      palette['blue'],
    'cyan':                      palette['cyan'],
    'darkgray':                  palette['darkgray'],
    'gray':                      palette['gray'],
    'green':                     palette['green'],
    'lightgray':                 palette['lightgray'],
    'magenta':                   palette['magenta'],
    'orange':                    palette['orange'],
    'purple':                    palette['purple'],
    'red':                       palette['red'],
    'teal':                      palette['teal'],
    'yellow':                    palette['yellow'],
    # 'brown'
    # 'lime'
    # 'olive'
    # 'pink'
    # 'violet'

    # Core colors
    'cursor':                    palette['cursor'],           # Cursor color
    'background':                palette['background'],       # Background of main canvas
    'foreground':                palette['foreground'],       # Default text color
    'selection':                 palette['yellow'],           # Background color of selected text/math
    'selectiontext':             palette['background'],       # Text color of selected text
    'selectionmath':             palette['background'],       # Text color of selected math
    'bottomarea':                palette['background'],       # Background color below end of document (if bottom-scrolling is enabled)
    'inlinecompletion':          palette['foreground'],       # Inline completion color for the unambigous part
    'nonuniqueinlinecompletion': palette['gray'],             # Inline completion color for the non-unique part

    # Collapsible insets
    # ------------------
    # label color:        text color of attached *button* label
    # text color:         text color of content box
    # background color:   background color of content box
    # frame color:        frame color of content box

    # Default colors for content of collapsible insets (eg. notes, listings, options)
    'collapsible':               palette['yellow'],           # Label color for button
    'collapsibleframe':          palette['darkgray'],         # Frame color for content boxes (applies to almost all non-button frames)

    # Colors for buttons
    'buttonbg':                  palette['darkgray'],         # Background color for all buttons (including citations, references, labels)
    'buttonframe':               palette['darkgray'],       # Frame color for all buttons
    'buttonhoverbg':             palette['darkgray'],         # Background color for all buttons under focus

    # Overwriting defaults for collapsibles
    'note':                      palette['green'],            # Label color for notes (button text)
    'notebg':                    palette['darkgray'],       # Background color for notes content
    'comment':                   palette['green'],            # Label color for comments (button text)
    'commentbg':                 palette['darkgray'],       # Background color for comments
    'greyedout':                 palette['green'],            # Label color for greyedout inset (button text)
    'greyedouttext':             palette['gray'],             # Text color for greyedout inset
    'greyedoutbg':               palette['darkgray'],       # Background color for greyedout inset
    'shaded':                    palette['background_dark'],  # Background color of shaded box
    'listingsbg':                palette['background_dark'],  # Background color of listings inset

    'branchlabel':               palette['magenta'],           # Label color for branches (button text)
    'footlabel':                 palette['blue'],             # Label color for footnotes (button text)
    'indexlabel':                palette['teal'],             # Label color for index inset (button text)
    'marginlabel':               palette['blue'],             # Label color for margin notes (button text)
    'urllabel':                  palette['gray'],             # Label color for URL inset (button text)
    'urltext':                   palette['magenta'],          # Text color for URL inset

    # Command insets
    'command':                   palette['orange'],           # Label color for command inset (eg. cites, refs, labels)
    'commandbg':                 palette['background'],       # Background color for non-editable buttons
    'commandframe':              palette['darkgray'],         # Frame color for non-editable buttons
    'command_broken':            palette['foreground'],       # Label color for broken inset (eg. broken references)
    'commandbg_broken':          palette['red'],              # Background color for broken inset
    'commandframe_broken':       palette['foreground'],       # Frame color for broken inset
    'buttonhoverbg_broken':      palette['darkred'],          # Background color for broken inset button under focus

    'latex':                     palette['cyan'],             # Text color for ERT (also used for beamer frame/section)
    'textlabel1':                palette['blue'],             # Label color 1 for text (layout) labels (eg. beamer frame title, beamer note)
    'textlabel2':                palette['green'],            # Label color 2 for text (layout) labels (eg. beamer example block, corollary))
    'textlabel3':                palette['magenta'],          # Label color 3 for text (layout) labels (eg. beamer only, visible, etc)
    'preview':                   palette['foreground'],       # Text color used for previews (e.g., mathpreview)

    'graphicsbg':                palette['background'],       # Background color for graphics inset
    'math':                      palette['foreground'],       # Text color for math inset
    'mathbg':                    palette['background'],       # Background color for math inset
    'mathframe':                 palette['darkgray'],         # Frame color for math inset under focus
    'mathcorners':               palette['background'],       # Frame color for math inset not under focus
    'mathline':                  palette['darkgray'],         # Line colors for math inset (eg. arrays, matrices)

    # Math macros
    'mathmacrobg':               palette['background'],       # Background color for math macro inset
    'mathmacrohoverbg':          palette['darkgray'],         # Background color for math macro inset under focus
    'mathmacrolabel':            palette['gray'],             # Label color for math macro inset
    'mathmacroframe':            palette['darkgray'],         # Frame color for math macro inset
    'mathmacroblend':            palette['foreground'],       # Blended color for math macro inset
    'mathmacrooldarg':           palette['gray'],             # Macro template color for old parameters
    'mathmacronewarg':           palette['foreground'],       # Macro template color for new parameters

    'insetbg':                   palette['darkgray'],         # Background color for inset marker
    'insetframe':                palette['yellow'],           # Frame color for inset marker
    'insetlabel':                palette['foreground'],       # Label color for inset marker

    'error':                     palette['darkred'],          # Text color for latex errors
    'phantomtext':               palette['gray'],             # Text color for phantom inset
    'special':                   palette['red'],              # Text color for special chars
    'depthbar':                  palette['darkgray'],         # Depth bars in the margin (for nested environments)
    'scroll':                    palette['red'],              # Color that indicates when a row can be scrolled
    'language':                  palette['magenta'],          # Color for marking foreign language words
    'eolmarker':                 palette['gray'],             # Text color for end of line marker
    'added_space':               palette['gray'],             # Text color for spaces marker
    'paragraphmarker':           palette['darkgray'],         # Text color for pilcrow marker (¶)

    'appendix':                  palette['gray'],             # Begin appendix indicator color
    'newpage':                   palette['gray'],             # Newpage indicator color
    'pagebreak':                 palette['gray'],             # Pagebreak indicator color
    'bookmark':                  palette['blue'],             # Bookmark indicator color

    'tabularline':               palette['gray'],             # Table line color
    'tabularonoffline':          palette['gray'],             # Table on/off line color

    'previewframe':              palette['orange'],           # Frame color for preview inset (around ERT)
    'regexpframe':               palette['green'],            # Frame color for regexp inset

    # Track changes
    'changebar':                 palette['blue'],             # Changebar color in left margin
    'changedtextauthor1':        palette['blue'],             # Changed text color for N-th author
    'changedtextauthor2':        palette['magenta'],          #   - " -
    'changedtextauthor3':        palette['cyan'],             #   - " -
    'changedtextauthor4':        palette['green'],            #   - " -
    'changedtextauthor5':        palette['yellow'],           #   - " -
    'changedtextcomparison':     palette['blue'],             # Changed text color for document comparison
    'deletedtextmodifier':       palette['background'],       # Deleted text modifying color for brightness modulation (blended with author color)
    # 'deletedtext':             palette['red'],              # Deleted text color (exported output)
    # 'addedtext':               palette['green'],            # Added text color (exported output)
}  # fmt: skip


def quote(s):
    return '"' + s + '"'


# export the colorscheme
path = 'out'
file = os.path.join(path, colors + '_lyx_cs')

if not os.path.exists(path):
    os.makedirs(path)

with open(file, 'w') as o:
    o.write('# ' + colors + ' colorscheme for LyX\n')

with open(file, 'a') as o:
    for color, value in colorscheme.items():
        _c = ('\set_color', quote(color), *2 * (quote(value),))
        o.write(' '.join(_c) + '\n')
