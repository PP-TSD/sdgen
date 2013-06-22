#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import sys

sys.path.append(os.path.join('..', 'src'))

from sdgen import to_png

EXAMPLES_DIR = '.'
OUTPUT_DIR = sys.argv[1] if len(sys.argv) == 2 else 'output'
EXAMPLES_EXT = '.json'

if __name__ == '__main__':
    print "Generating examples from JSON files..."

    examples = sorted([os.path.join(EXAMPLES_DIR, f) for f in os.listdir(EXAMPLES_DIR) if f.endswith(EXAMPLES_EXT)])
    for example in examples:
        print "processing " + example
        # load data
        example_file = open(example, 'r')
        m = json.load(example_file)

        name = m['name']

        conf = {
            'png': {
                'ppi': 225
            }
        }
        r = to_png(m, OUTPUT_DIR, conf=conf, overwrite=True)

    print "done"
