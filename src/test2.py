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
    data2 = {
        "view": "Terminal",
        "value": "KUBKED"
    }
    b = PNGBuilder()
    b.generate(data2, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.png'))


if __name__ == '__main__':
    main()