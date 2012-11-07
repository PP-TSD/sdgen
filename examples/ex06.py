#!/usr/bin/env

# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/') # remove this if sdgen is accessible in your os
from sdgen import *

data = {
    "view": "Group",
    "name": "Alternation example",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            'children': [
                 {"view": "Terminal", "value": "B"},
                 {"view": "Terminal", "value": "C"}
            ],
            "name": "Alternation BC",
            "view": "Alternation"
        },
        {"view": "Terminal", "value": "D"}
    ]
}

result = as_png(data, sys.argv[1])
print result[0][1].encode('utf-8')
