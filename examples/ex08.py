# -*- coding: utf-8 -*-
import sys
sys.path.append('.')
from sdgen.svg import *

data = {
    "view": "Group",
    "name": "Example of QuantityAbove",
    "children": [
        {"view": "Terminal", "value": "A"},
        {
            'children': [
                {"view": "Terminal", "value": "B"}
            ],
            "name": "Quantity Above B",
            "view": "QuantityAbove",
            "value": "0..n"
        },
        {"view": "Terminal", "value": "C"}
    ]
}

result = as_svg(data, sys.argv[1])
print result[0][1].encode('utf-8')
