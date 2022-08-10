# lyx-colorcheme-brewer

A colorscheme brewer for LyX. It takes standard 16-color terminal palettes and turns them into
LyX colorschemes.

## Ready-to-use color schemes

The following schemes are currently pre-packaged and ready to be used:
* onedark
* gruvbox

To use them, either manually copy the contents of the scheme files from the [out](out)
folder into the "colors" section of the `preferences` file in your LyX configuration
folder. Or, use the bundled `install_colorscheme.sh` script:
```
./install_colorscheme.sh out/scheme_name filepath/to/preferences
```

## Making new color schemes

To create a new colorscheme, place the palette containing the color definitions inside
the `colors` folder, and then run: 
```
make_colorscheme.py scheme_name
```
This will create a LyX colorscheme inside the `out` folder.
