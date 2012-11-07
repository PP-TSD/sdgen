# -*- coding: utf-8 -*-
import sys
sys.path.append('.')
from sdgen.svg import *

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

result = as_svg(data, sys.argv[1])
print result[0][1].encode('utf-8')
