# -*- coding: utf-8 -*-
import sys
sys.path.append('.')
from sdgen.svg import *

data = {
    "view": "Group",
    "name": "Inverse Terminal example",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            'children': [
                {"view": "Terminal", "value": "B"},
                {"view": "Terminal", "value": "C"},
                {"view": "Terminal", "value": "D"}
            ],
            "name": "Inv Terminal BCD",
            "view": "InvTerminal"
        },
        {"view": "Terminal", "value": "E"}
    ]
}

result = as_svg(data, sys.argv[1])
print result[0][1].encode('utf-8')
