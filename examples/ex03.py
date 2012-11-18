#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/') # remove this if sdgen is accessible in your os
from sdgen import *

data = {
    "view": "Group",
    "name": "Nonterminal example",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            'children': [
                {
                    'children': [
                        {"view": "Terminal", "value": "B"},
                        {"view": "Terminal", "value": "C"}
                    ],
                    "name": "Non Terminal C",
                    "view": "NonTerminal"
                }
            ],
            "name": "Quantity Above Non Terminal",
            "view": "QuantityAbove",
            "value": "0..n"
        },
        {"view": "Terminal", "value": "D"}
    ]
}

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) == 2 else "."
    result = to_png(data, path)
    print result[0][1].encode('utf-8')
