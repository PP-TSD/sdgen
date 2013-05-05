# -*- coding: utf-8 -*-
# import os
import json

# application config
_default_font_paths = [
    "/usr/share/fonts/TTF/",
    "C:\\WINDOW\\Fonts\\",
    "/usr/share/fonts/truetype/"
]
config = {
    "fonts": {
        "directories": _default_font_paths[:]
    }
}
render_config = config  # backward compatibility


def safeget(d, path, default=None):
    """
    Returns value from dict d with keys from path, separeted by dot.
    If key-path is not in dict, returns None.
    """
    tmp = d
    for key in path.split("."):
        if isinstance(tmp, dict) and key in tmp:
            tmp = tmp[key]
        else:
            return default
    return tmp


def load_config(data):
    """
    Loads render config to render_config variable
    """
    global config

    if data:
        if isinstance(data, file):
            data = json.load(data)
        assert isinstance(data, dict)
        config.update(data)

        # append font directories to default
        data_fonts_dir = safeget(data, "fonts.directories", [])
        fonts_dirs = _default_font_paths[:]
        fonts_dirs[0:0] = data_fonts_dir
        config["fonts"]["directories"] = fonts_dirs
