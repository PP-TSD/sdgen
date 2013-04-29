# -*- coding: utf-8 -*-
import argparse
import json
import os
# change to proper import when svg package will be modified
from .builder import Builder as SVGBuilder
from .png.png_builder import PNGBuilder
from . import config


DATA_FILE_INCORRECT = -1
CONFIG_FILE_INCORRECT = -2
CONFIG_FILE_UNEXISTS = -3
OUTPUT_PATH_INCORRECT = -4

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
        '--format': {
            'default': 'png',
            'choices': _builders.keys(),
            'help': 'output format, ex. "png"'
        },
        '--overwrite': {
            'action': 'store_true',
            'help': 'overwrite existing output files'
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
        data = json.loads(data, encoding="utf-8")
    except ValueError:
        print "Data file doesn't consist valid JSON."
        exit(DATA_FILE_INCORRECT)

    return _main(data=data,
                 format=args.format,
                 input_path=args.input.name,
                 output_dir=args.output,
                 render_config=args.render_config,
                 overwrite=args.overwrite)


def _main(data, output_dir=None, format='png', input_path='sdgen', render_config=None, overwrite=False):
    try:
        config.load(render_config)
    except ValueError:
        print "Config file doesn't consist valid JSON."
        exit(CONFIG_FILE_INCORRECT)
    except IOError:
        print "Config file doesn't exists."
        exit(CONFIG_FILE_UNEXISTS)

    if output_dir is not None:
        if not os.path.isdir(output_dir):
            if not os.path.isdir(os.path.dirname(output_dir)) or\
                    os.path.exists(output_dir):
                print "Path to the output is not correct"
                exit(OUTPUT_PATH_INCORRECT)
            else:
                os.mkdir(output_dir)

    builder = _builders[format]()
    return builder.generate(data=data, input_path=input_path, output_dir=output_dir, overwrite=overwrite)


def to_png(data, path=None, conf=None, overwrite=False):
    """
    .. deprecated:: 0.0.3

    Generate a png image(s). This function can generate multiple images.
    :param data: input data
    :type data: dict
    :param path: path were to save files; if the value is None no file is saved,
        overwriting is forbidden (raise exception)
    :type path: str
    :param conf: render configuration to substitute the default one
    :type conf: dict
    :return: a list of tuples, each tuple contains two fields: a name and an image in png format
    :rtype: list
    """
    return _main(data, format='png', output_dir=path, render_config=conf, overwrite=overwrite)


if __name__ == '__main__':
    main()
