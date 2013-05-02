#!/usr/bin/env python

import json
import os
import sys
import string

sys.path.append('../src')

from sdgen import to_png

TEMPLATE_HEADER = """========
Examples
========

Below there are some examples of using Syntax Diagram Generator to generate images.

"""

TEMPLATE_NAME = """%s
%s

.. literalinclude:: %s
   :language: json
   :linenos:

"""

TEMPLATE_IMAGE = """
.. image:: %s

"""

GENERATED_DIR = '_generated'
EXAMPLES_GENERATED_DIR = os.path.join('source', GENERATED_DIR)
EXAMPLES_TXT = os.path.join('source', '_static', 'examples.txt')
EXAMPLES_DIR = os.path.join('..', 'examples')
EXAMPLES_EXT = '.json'


if __name__ == '__main__':
    print "Generating examples...",

    txt = open(EXAMPLES_TXT, "w")

    txt.write(TEMPLATE_HEADER)

    examples = sorted([os.path.join(EXAMPLES_DIR, f) for f in os.listdir(EXAMPLES_DIR) if f.endswith(EXAMPLES_EXT)])
    for example in examples:
        # load data
        example_file = open(example, 'r')
        m = json.load(example_file)

        name = m['name']
        path_from_generated = os.path.join('..', '..', example)

        # put json contentof an example
        txt.write(TEMPLATE_NAME % (name, '-' * len(name), path_from_generated))

        conf = {
            'png': {
                'dpi': 100
            }
        }

        # add images
        r = to_png(m, EXAMPLES_GENERATED_DIR, conf=conf, overwrite=True)

        for i in r:
            filename = i[0].replace(' ', '_').lower() + ".png"
            img_path = os.path.join('..', GENERATED_DIR, filename)
            txt.write(TEMPLATE_IMAGE % img_path)

    print "done"
