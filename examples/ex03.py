# -*- coding: utf-8 -*-
import sys
sys.path.append('.')
from sdgen.svg import *

data = {
    "view": "Group",
    "name": "Example of NonTerminal",
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

result = as_svg(data, sys.argv[1])
print result[0][1].encode('utf-8')
