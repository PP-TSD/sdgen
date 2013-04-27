# -*- coding: utf-8 -*-
import argparse
import json
import os
# change to proper import when svg package will be modified
from .builder import Builder as SVGBuilder
from .png.png_builder import PNGBuilder
from . import config


_builders = {
    'svg': SVGBuilder,
    'png': PNGBuilder,
}

def main():
    """Entry point with args parser."""
    parser = argparse.ArgumentParser(description='Generate syntax diagram.')
    
    arguments = {
        'input': {
            'type': file,
            'help': 'data file in JSON format'
        },
        'output': {
            'help': 'path to output directory'
        },
        '--render-config': {
            'type': file,
            'metavar': 'CONFIG_FILE',
            'help': 'config file in json format'
        },
        '--formnat': {
            'default': 'png',
            'choices': _builders.keys(),
            'help': 'output format, ex. "png"'
        }
    }
    # add arguments specified above to command parser
    for argument in arguments:
        parser.add_argument(argument, **arguments[argument])
    # parse arguments from sys.argv into args object
    args = parser.parse_args()
    
    # read given input file (file will be closed at the end of function)
    data = args.input.read()
    try:
        data = json.loads(data)
    except ValueError:
        print "Data file doesn't consist valid JSON."
        exit(-1)
    return _main(data=data, format=args.format, input_path=args.input.name, output_dir=args.output, render_config=args.render_config)

def _main(data, output_dir, format='png', input_path='sdgen', render_config=None):
    try:
        config.load(render_config)
    except ValueError:
        print "Config file doesn't consist valid JSON."
        exit(-2)
    except IOError:
        print "Config file doesn't exists."
        exit(-3)

    if not os.path.isdir(output_dir):
        if not os.path.isdir(os.path.dirname(output_dir)) or\
                os.path.exists(output_dir):
            print "Path to the output is not correct"
            return -4
        else:
            os.mkdir(output_dir)

    builder = _builders[format]()
    return builder.generate(data=data, input_path=input_path, output_dir=output_dir)


def to_png(*args, **kwargs):
    return _main(format='png', *args, **kwargs)


if __name__ == '__main__':
    main()
