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

.. include:: %s
   :literal:

"""

TEMPLATE_IMAGE = """
.. image:: %s

"""

if __name__ == '__main__':
    print "Generating examples...",

    txt = open("source/_generated/examples.txt", "w")

    txt.write(TEMPLATE_HEADER)
    examples = [os.path.splitext(filename)[0]
                    for filename in os.listdir('../examples')
                    if filename.endswith('json')]
    for example in examples:
        # load data
        example_file = open('../examples/%s.json' % example, 'r')
        m = json.load(example_file)
        
        name = m['name']
        path = "../../../examples/%s.json" % example

        # put header and source code of an example
        txt.write(TEMPLATE_NAME % (name, '=' * len(name), path))

        # add images
        r = to_png(m, "source/_generated/")

        for i in r:
            filename = i[0].replace(' ', '_').lower() + ".png"

            txt.write(TEMPLATE_IMAGE % filename)

    print "done"
