#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join('..', '..', 'src'))

import sdgen

data = {
    "view": "Group",
    "name": "Spaces example",
    "children": [
        {"view": "Terminal", "value": " "},
        {
            'children': [
                {"view": "Terminal", "value": " B "},
                {"view": "Terminal", "value": " C   "},
                {"view": "Terminal", "value": " E F  "},
                {"view": "Terminal", "value": "G H I"},
            ],
            "name": "Alternation BC    ",
            "view": "Alternation"
        },
        {"view": "Terminal", "value": " D"}
    ]
}

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) == 2 else "output"
    result = sdgen.to_png(data, path, overwrite=True)
