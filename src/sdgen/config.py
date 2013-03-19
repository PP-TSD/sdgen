# -*- coding: utf-8 -*-
import ConfigParser
import os

# climb up in directories path (level must be positive integer)
dir_up = lambda path, level: (path if not level else
                              dir_up(os.path.dirname(path), level-1))

config = ConfigParser.SafeConfigParser()
# ./src/sdgen/config.py -> ./var/config.ini
file_path = lambda depth: os.path.join(dir_up(os.path.abspath(__file__), depth), 'var', 'config.ini')
config.read(file_path(2))
config.read(file_path(3))