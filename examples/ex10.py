# -*- coding: utf-8 -*-
import sys
sys.path.append('.')
from sdgen.svg import *

data = {
    "view": "Group",
    "name": "Complex detour diagram",
    "children": [
        {"view": "Terminal", "value": "A"},
	{
		"view": "Detour",
		"children": [
			{
		 		"children": [
					{
						'children': [
							{"view": "Terminal", "value": "B"},
							{"view": "Terminal", "value": "C"}
						],
						"name": "B C",
						"view": "NonTerminal"
					}
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

result = as_svg(data, sys.argv[1])
print result[0][1].encode('utf-8')
