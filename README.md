Syntax Diagram Generator
========================

Installation
------------

    python setup.py install

Getting started
---------------

First, execute some examples:

    python examples/ip.py > ip.svg

Then, generate simple diagram for IP grammar:

    from sdgen import as_svg

    data = {
        "view": "Group",
        "name": "IP address",
        "children": [
            {"value": "0..255", "view": "Terminal"},
            {"value": "0..255", "view": "Terminal"},
            {"value": "0..255", "view": "Terminal"},
            {"value": "0..255", "view": "Terminal"}
        ]
    }

    retval = to_svg(data)
    print retval[0][1]

Authors
-------

    See AUTHORS file.

Licence
-------

Syntax Diagram Generator is released under the MIT license. See LICENSE file.

Syntax Diagram Generator includes the following libraries which are released under their own license:
- pysvg (BSD, see: http://http://codeboje.de/pysvg/)
- cairosvg (LGPL version 3, see: http://cairosvg.org/)
