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
    },
    "png": {
        "dpi": 300,
        "scale": 1
    }
}
render_config = config  # backward compatibility

# def dir_up(path, level):
#     """
#     climb up in directories path (level must be positive integer)
#     """
#     return path if not level else dir_up(os.path.dirname(path), level-1)


# def file_path(depth, names):
#     return os.path.join(dir_up(os.path.abspath(__file__), depth), *names)


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


# def load_config():
#     global config

#     if not config:
#         config = ConfigParser.SafeConfigParser()
#         # ./src/sdgen/config.py -> ./var/config.ini
#         config_path = ('var', 'config.ini')
#         # try to load from two different levels
#         config.read(file_path(2, config_path))
#         config.read(file_path(3, config_path))


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
        fonts_dirs.extend(data_fonts_dir)
        config["fonts"]["directories"] = fonts_dirs
