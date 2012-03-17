# -*- coding: utf-8 -*-
import sys
sys.path.append('.')
from sdgen.svg import *

data = {
    "view": "Group",
    "name": "HTTP Address",
    "children": [
        {"view": "Terminal", "value": "http"},
        {
            "view": "Detour",
            "children": [
                {"view": "Terminal", "value": "s"}
            ]
        },
        {"view": "Terminal", "value": "://"},
        {
            "view": "Detour",
            "children": [
                {
                    "view": "Group",
                    "name": u"Phrase with at",
                    "children": [
                        {
                            "view": "QuantityAbove",
                            "value": "1..",
                            "children": [
                                {
                                    "view": "InvTerminal",
                                    "children": [
                                        {"view": "Terminal", "value": "a..z"}
                                    ]
                                }
                            ]
                        },
                        {"view": "Terminal", "value": ":"},
                        {
                            "view": "QuantityAbove",
                            "value": "1..",
                            "children": [
                                {
                                    "view": "InvTerminal",
                                    "children": [
                                        {"view": "Terminal", "value": "a..z"}
                                    ]
                                }
                            ]
                        },
                        {"view": "Terminal", "value": "@"}
                    ]
                }
            ]
        },
        {
            "view": "QuantityAbove",
            "value": "1..",
            "children": [
                {
                    "view": "Group",
                    "name": u"Phrase with dot",
                    "children": [
                        {
                            "view": "QuantityAbove",
                            "value": "1..",
                            "children": [
                                {
                                    "view": "InvTerminal",
                                    "children": [
                                        {"view": "Terminal", "value": "a..z"}
                                    ]
                                }
                            ]
                        },
                        {"view": "Terminal", "value": "."}
                    ]
                }
            ]
        },
        {
            "view": "QuantityAbove",
            "value": "2..",
            "children": [
                {
                    "view": "InvTerminal",
                    "children": [
                        {"view": "Terminal", "value": "a..z"}
                    ]
                }
            ]
        },
        {
            "view": "Detour",
            "children": [
                {
                    "view": "Group",
                    "name": u"End",
                    "children": [
                        {"view": "Terminal", "value": ":"},
                        {
                            "view": "InvTerminal",
                            "children": [
                                {"view": "Terminal", "value": "0..65535"}
                            ]
                        }
                    ]
                }
            ]
        },
        {
            "view": "Detour",
            "children": [
                {"view": "Terminal", "value": "/"}
            ]
        }
    ]
}


result = as_svg(data)
print result[0][1].encode('utf-8')
