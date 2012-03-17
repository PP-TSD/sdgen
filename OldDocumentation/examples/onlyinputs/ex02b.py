{
    "view": "Group",
    "name": "Example of Detour element",
    "children": [
        {"view": "Terminal", "value": "A"},
	{
		"view": "Detour",
		"children": [
			{
		 		"children": [
					{"view": "Terminal", "value": "B"}
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
