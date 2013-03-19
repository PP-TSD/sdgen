import os
from sdgen.png.png_builder import PNGBuilder


def main():
    data = {
        "view": "Group",
        "name": "Terminal example",
        "children": [
        {
            "view": "Terminal",
            "value": "A"
        },
        {
            "view": "Terminal",
            "value": "B"
        },
        {
            "view": "Terminal",
            "value": "C"
        },
        {
            "view": "Terminal",
            "value": " "
        }
        ]
    }
    b = PNGBuilder()
    b.generate(data, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.png'), None)


if __name__ == '__main__':
    main()
