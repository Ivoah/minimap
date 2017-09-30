# minimap

Generate minimaps of your code

![example](https://raw.githubusercontent.com/Ivoah/minimap/master/minimap.png)

## Requirements

`minimap.py` requires Python 3.6 or greater

## Usage

```
minimap.py [-o OUTPUT [OUTPUT ...]] [-l LANGUAGE] [-s STYLE] [-w WIDTH]
           [-h HEIGHT] [--spacing SPACING] [--overwrite] files [files ...]
```

## Options

```
-o            Output file (or files). Must come after input files if listing multiple
-l            Select language to highlight for (if it can't autodetect)
-s            Select highlighting style (use `-s list` to list all styles)
-w            Width of each character in pixels
-h            Height of each character in pixels
--spacing     Number of pixels to insert between rows
--overwrite   Overwrite output file if it already exists
```
