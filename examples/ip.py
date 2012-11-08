#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/') # remove this if sdgen is accessible in your os
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

if __name__ == '__main__':
    retval = as_svg(data)
    print retval[0][1].encode('utf-8')
