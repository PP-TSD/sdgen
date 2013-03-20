# -*- coding: utf-8 -*-
import argparse
import json
import os

from .builder import Builder as SVGBuilder  # change to proper import when svg package will be modified
from .png.png_builder import PNGBuilder
from . import config


def main():
    builders = {
        'svg': SVGBuilder,
        'png': PNGBuilder,
    }

    parser = argparse.ArgumentParser(description='Generate syntax diagram.')
    parser.add_argument('input', type=file, help='data file in JSON format')
    #TODO: what to do with many output files
    parser.add_argument('output', help='path to output files')
    parser.add_argument('--config', type=file, metavar='CONFIG_FILE',
                        help='config file in json format')
    parser.add_argument('--format', default='svg', choices=builders.keys(),
                        help='output format')

    args = parser.parse_args()

    data = args.input.read()
    try:
        data = json.loads(data)
    except ValueError:
        print "Data file doesn't consist valid JSON."
        return -1

    try:
        config.load(args.config)
    except ValueError:
        print "Config file doesn't consist valid JSON."
        return -2
    except IOError:
        print "Config file doesn't exists."
        return -3

    if not os.path.isdir(args.output):
        if not os.path.isdir(os.path.dirname(args.output)) or\
                os.path.exists(args.output):
            print "Path to the output is not correct"
            return -4
        else:
            os.mkdir(args.output)

    builder = builders[args.format]()
    builder.generate(data=data, path=args.output)


if __name__ == '__main__':
    main()
