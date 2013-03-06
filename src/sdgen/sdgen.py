# -*- coding: utf-8 -*-
import argparse
import json
import os

from sdgen.svg import to_svg
from sdgen.png import to_png


def main():
    builders = {
        'svg': to_svg,
        'png': to_png,
    }
    
    parser = argparse.ArgumentParser(description='Generate syntax diagram.')
    parser.add_argument('input', type=file, help='data file in JSON format')
    #TODO: what to do with many output files
    parser.add_argument('output', type=argparse.FileType('w'),
                        help='path to output files')
    parser.add_argument('--config', type=file, metavar='CONFIG_FILE',
                        help='config file in json format')
    parser.add_argument('--format', default='svg', choices=converters.keys(),
                        help='output format')
    
    args = parser.parse_args()
    
    data = input.read()
    try:
        json.loads(data)
    except ValueError:
        print "Data file doesn't consist valid JSON."
        return -1
    
    config = None
    if args['config']:
        config = input.read()
        try:
            json.loads(config)
        except ValueError:
            print "Config file doesn't consist valid JSON."
            return -2
    
    if not os.path.isdir(args['output']):
        if not os.path.isdir(os.path.dirname(args['output'])) or\
                os.path.exists(args['output']):
            print "Path to the output is not corrected"
            return -3
        else:
            os.mkdir(args['output'])
    
    result = builders[args['config']](data=data, path = args['output'],
                                      config=config)
    output.write(result)
