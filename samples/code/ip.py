#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join('..', '..', 'src'))

import sdgen

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
    path = sys.argv[1] if len(sys.argv) == 2 else "."
    result = sdgen.to_png(data, path, overwrite=True)
