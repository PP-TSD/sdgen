{
    "view": "Group",
    "name": "Example of Detour element",
    "children": [
        {"view": "Terminal", "value": "A"},
	{
	     "children" : [
			{
				"view": "Detour",
            			"children": [
               		 		{
						'children': [
							{"view": "Terminal", "value": "B"}
						],
						"name": "Quantity Above B",
						"view": "QuantityAbove",
						"value": "0..n"
					}
            			]
			}
             ],
 	     "name": "Quantity above Detour",
	     "view": "QuantityAbove",
	     "value": "a..z",
	},
	{"view": "Terminal", "value": "C"}
     ]
}
