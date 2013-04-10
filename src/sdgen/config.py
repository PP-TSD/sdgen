# -*- coding: utf-8 -*-
import ConfigParser
import os
import json

config = None  # application config from .ini file
render_config = {
    'png': {
        'dpi': 70
    }
}  # render config from .json file


def dir_up(path, level):
    """
    climb up in directories path (level must be positive integer)
    """
    return path if not level else dir_up(os.path.dirname(path), level-1)


def file_path(depth, names):
    return os.path.join(dir_up(os.path.abspath(__file__), depth), *names)


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


def load_config():
    global config

    if not config:
        config = ConfigParser.SafeConfigParser()
        # ./src/sdgen/config.py -> ./var/config.ini
        config_path = ('var', 'config.ini')
        # try to load from two different levels
        config.read(file_path(2, config_path))
        config.read(file_path(3, config_path))


def load_render_config(data):
    """
    Loads render config to render_config variable
    """
    global render_config

    if not render_config:
        if isinstance(data, file):
            data = json.load(data)
        assert isinstance(data, dict)
        render_config.update(data)


def load(render_config_path):
    load_config()
    load_render_config(render_config_path)


# try to load application config by default
if not config:
    load_config()
