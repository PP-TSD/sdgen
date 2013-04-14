#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/') # remove this if sdgen is accessible in your os
from sdgen import *

data = {
    "view": "Group",
    "name": "Complex detour diagram",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            "view": "Detour",
            "children": [
                {
                    "children": [
                        {
                            'children': [
                                {"view": "Terminal", "value": "B"},
                                {"view": "Terminal", "value": "C"}
                            ],
                            "name": "B C",
                            "view": "NonTerminal"
                        }
                    ],
                    "name": "Quantity Above B",
                    "view": "QuantityAbove",
                    "value": "0..2"
                },
            ]
        },
        {"view": "Terminal", "value": "C"}
    ]
}

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) == 2 else "."
    result = to_png(data, path)
    print result[0][1].encode('utf-8')
