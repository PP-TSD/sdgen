#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
sys.path.append('../src/') # remove this if sdgen is accessible in your os
from sdgen import *

data = {
    "view": "Group",
    "name": "Nested groups example",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            'children': [
                {"view": "Terminal", "value": "C1"},
                {
                    "view": "Detour",
                    'children': [
                        {
                           'children': [
                                {"view": "Terminal", "value": "C"},
                                {"view": "Terminal", "value": "D"},
                                {"view": "Terminal", "value": "E"}
                           ],
                           "name": "Inv Terminal CD",
                           "view": "InvTerminal"
                        }
                    ],
                },
                {"view": "Terminal", "value": "C2"},
            ],
            "name": "Internal group",
            "view": "Group"
        },
        {"view": "Terminal", "value": "B"}
    ]
}

if __name__ == '__main__':
    result = to_png(data, sys.argv[1])
    print result[0][1].encode('utf-8')
