import sys
sys.path.append('.')
from sdgen.svg import *

data = {
    "view": "Group",
    "name": "Simple A->B",
    "children": [
	{"view": "Terminal", "value": "A"},
	{"view": "Terminal", "value": "B"},
	{"view": "Terminal", "value": "C"},
	{"view": "Terminal", "value": " "}
     ]
}

result = as_png(data, sys.argv[1])
print result[0][1].encode('utf-8')
