#!/usr/bin/env python

import imp
import sys
import string

sys.path.append('../examples')
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

examples = ["ex01", "ex05", "ex07", "ex06", "ex02", "ex10", "ex04", "ex03", "ex09"]

if __name__ == '__main__':
    print "Generating examples...",

    txt = open("source/_generated/examples.txt", "w")

    txt.write(TEMPLATE_HEADER)

    for example in examples:
        # load data
        m = imp.load_source('m', '../examples/%s.py' % example)

        name = m.data['name']
        path = "../../../examples/%s.py" % example

        # put header and source code of an example
        txt.write(TEMPLATE_NAME % (name, '=' * len(name), path))

        # add images
        r = to_png(m.data, "source/_generated/")

        for i in r:
            filename = i[0].translate(string.maketrans(' ', '_')) + ".png"

            txt.write(TEMPLATE_IMAGE % filename)

    print "done"
