#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os.path
import argparse

import pygments
import pygments.styles
import pygments.lexers
import pygments.formatter

from PIL import Image
from PIL import ImageDraw


def main():
    parser = argparse.ArgumentParser(add_help = False)
    parser.add_argument('files', nargs = '+')
    parser.add_argument('-o', '--output', nargs = '+')
    parser.add_argument('-l', '--language', '--lang')
    parser.add_argument('-s', '--style', default = 'monokai')
    parser.add_argument('-w', '--width', type = int, default = 3)
    parser.add_argument('-h', '--height', type = int, default = 5)
    parser.add_argument('--spacing', type = int, default = 1)
    parser.add_argument('--tab-width', type = int, default = 4)
    parser.add_argument('--overwrite', action="store_true")

    args = parser.parse_args()

    if args.style == 'list':
        print('Available styles:', ', '.join(pygments.styles.get_all_styles()))
        sys.exit(0)

    style = pygments.styles.get_style_by_name(args.style)
    colors = {t: '#' + (s['color'] or '777') for t, s in style}

    if args.output is None:
        args.output = [os.path.splitext(os.path.basename(filename))[0] + '.png' for filename in args.files]

    if len(args.output) > 0 and len(args.files) != len(args.output):
        print(f'{sys.argv[0]}: error: output must have the same number of arguments as input')
        sys.exit(1)

    for filename, output in zip(args.files, args.output):
        if not args.overwrite and os.path.exists(output):
            print(f'{sys.argv[0]}: error: "{output}" already exists')
            sys.exit(1)

        with open(filename, 'r') as f:
            code = f.read()
        if args.language:
            lexer = pygments.lexers.get_lexer_by_name(args.language)
        else:
            lexer = pygments.lexers.get_lexer_for_filename(filename)

        tokens = list(pygments.lex(code, lexer))

        lines = ''.join(map(lambda t: t[1], tokens)).split('\n')
        width = max(map(len, lines))*args.width
        height = (len(lines) - 1)*(args.height + args.spacing) - args.spacing

        img = Image.new('RGB', (width, height), style.background_color)
        draw = ImageDraw.Draw(img)

        x = 0
        y = 0
        for ttype, token in tokens:
            for c in token:
                if c == '\n':
                    x = 0
                    y += args.height + args.spacing
                elif c == ' ':
                    x += args.width
                elif c == '\t':
                    x += args.width*args.tab_width
                else:
                    draw.rectangle([(x, y), (x + args.width - 1, y + args.height - 1)], colors[ttype])
                    x += args.width

        img.save(output)


if __name__ == '__main__':
    main()
