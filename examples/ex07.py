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

result = to_png(data, sys.argv[1])
print result[0][1].encode('utf-8')
