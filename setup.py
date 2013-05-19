# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

PACKAGE_DIR = 'src'

def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
    name="sdgen",
    version='0.0.5',
    author=read("AUTHORS"),
    keywords="syntax diagram generator",
    url="https://github.com/PP-TSD/sdgen",
    install_requires=['pil'],
    package_dir={'': PACKAGE_DIR},
    long_description=read("README.md"),
    packages=find_packages(PACKAGE_DIR,
                           exclude=['ez_setup', 'examples', 'tests']),
    # data_files=[
    #     ('var', [
    #         os.sep.join(('var', 'config.ini')),
    #         os.sep.join(('var', 'render_config.json')),
    #     ]),
    # ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'sdgen = sdgen.main:main',
        ]
    }
)
