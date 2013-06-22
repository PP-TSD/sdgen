#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join('..', '..', 'src'))

import sdgen


def main():
    data = {
        "view": "Terminal",
        "name": "Terminal marked example",
        "value": u"Zażółć gęślą jaźń",
        "mark": "yes"
    }
    conf = {
        "terminal": {
            "padding": 8
        }
    }
    path = sys.argv[1] if len(sys.argv) == 2 else "output"
    images = sdgen.to_png(data, path=path, conf=conf, overwrite=True)
    return images

if __name__ == '__main__':
    main()
