#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join('..', '..', 'src'))

import sdgen

data = {
    "view": "Group",
    "name": "Sequence example",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            'children': [
                {"view": "Terminal", "value": "B"},
                {"view": "Terminal", "value": "C"},
                {"view": "Terminal", "value": "D"}
            ],
            "name": "Sequence BCD",
            "view": "Sequence"
        },
        {"view": "Terminal", "value": "E"}
    ]
}

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) == 2 else "."
    result = sdgen.to_png(data, path, overwrite=True)
