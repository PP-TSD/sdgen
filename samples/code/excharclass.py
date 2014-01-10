#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join('..', '..', 'src'))

import sdgen

data = {
    "view": "Sequence",
    "name": "excharclass",
    "children": [
        {
            "children": [
                {"view": "Header", "value": "not:"},
                {"view": "Terminal", "value": "A..C"},
                {"view": "Terminal", "value": " "}
            ],
            "name": "Inv Terminal BCD",
            "view": "InvTerminal"
        }
    ]
}

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) == 2 else "output"
    result = sdgen.to_png(data, path, overwrite=True)
