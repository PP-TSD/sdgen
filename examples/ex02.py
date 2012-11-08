#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/') # remove this if sdgen is accessible in your os
from sdgen import *

data = {
    "view": "Group",
    "name": "Detour example",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            "view": "Detour",
            "children": [
                {
                    "children": [
                        {"view": "Terminal", "value": "B"}
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
    result = to_png(data, sys.argv[1])
    print result[0][1].encode('utf-8')
