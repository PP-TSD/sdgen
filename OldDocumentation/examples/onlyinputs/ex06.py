{
    "view": "Group",
    "name": "Example of Alternation",
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
