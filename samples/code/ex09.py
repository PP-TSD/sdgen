#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join('..', '..', 'src'))

import sdgen

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
    path = sys.argv[1] if len(sys.argv) == 2 else "."
    result = sdgen.to_png(data, path, overwrite=True)
