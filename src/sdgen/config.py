# -*- coding: utf-8 -*-
import ConfigParser
import os
import json

config = None
render_config = {}


def dir_up(path, level):
    """
    climb up in directories path (level must be positive integer)
    """
    return path if not level else dir_up(os.path.dirname(path), level-1)


def file_path(depth, names):
    return os.path.join(dir_up(os.path.abspath(__file__), depth), *names)


def load_config():
    global config

    if not config:
        config = ConfigParser.SafeConfigParser()
        # ./src/sdgen/config.py -> ./var/config.ini
        config_path = ('var', 'config.ini')
        config.read(file_path(2, config_path))
        config.read(file_path(3, config_path))


def load_render_config(data=None):
    global render_config

    if not render_config:
        default_config_path = ('var', 'render_config.json')
        if data:
            json_data = data
        else:
            json_data = open(file_path(3, default_config_path))
        render_config = json.load(json_data)


def load(render_config_path):
    load_config()
    load_render_config(render_config_path)


if not config:
    load_config()
