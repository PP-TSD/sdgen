# -*- coding: utf-8 -*-
import sys
sys.path.append('.')
from sdgen.svg import *

data = {
    "view": "Group",
    "name": "Example of nested groups",
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

result = as_svg(data, sys.argv[1])
print result[0][1].encode('utf-8')
