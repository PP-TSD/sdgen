#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/') # remove this if sdgen is accessible in your os
from sdgen import *

data = {
    "view": "Group",
    "name": "Return example",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            "children" : [
                {
                    'children': [
                        {
                            'children': [
                                {"view": "Terminal", "value": "B"}
                            ],
                            "name": "Quantity Above B",
                            "view": "QuantityAbove",
                            "value": "0..11"
                        },
                        {"view": "Terminal", "value": "C"}
                    ],
                    "name": "Return BC",
                    "view": "Return"
                }
            ],
            "name": "Quantity above Return",
            "view": "QuantityAbove",
            "value": "0..5",
        },
        {"view": "Terminal", "value": "D"}
    ]
}

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) == 2 else "."
    result = to_png(data, path)
    print result[0][1].encode('utf-8')
