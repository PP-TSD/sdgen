#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join('..', '..', 'src'))

import sdgen

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
    result = sdgen.to_png(data, path, overwrite=True)
