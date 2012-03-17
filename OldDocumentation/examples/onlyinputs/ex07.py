{
    "view": "Group",
    "name": "Example of Return",
    "children": [
        {"view": "Terminal", "value": "A"},
	{
	     "children" : [
			{
				'children': [
					{
						'children': [
							{"view": "Terminal", "value": "B"}
						],
						"name": "Quantity Above B",
						"view": "QuantityAbove",
						"value": "0..11"
					},
					{"view": "Terminal", "value": "C"}
				],
				"name": "Return BC",
				"view": "Return"
			}
             ],
 	     "name": "Quantity above Return",
	     "view": "QuantityAbove",
	     "value": "0..5",
	},
	{"view": "Terminal", "value": "D"}
     ]
}
