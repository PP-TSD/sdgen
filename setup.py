import os
from setuptools import setup, find_packages

def read(file_name):
	return open(os.path.join(os.path.dirname(__file__), file_name)).read()

setup(
	name = "sdgen",
	version = "0.0.1",
	author = "Tomasz Zurkowski, Piotr Slatala, Marek Kuzora, Anna Fenster",
	author_email = "doriath88@gmail.com piotr@sepio.pl marek.kuzora@gmail.com noireffe@gmail.com",
	description = "",
	license = "MIT",
	zip_safe = False,
	keywords = "diagram generator",
	url = "https://github.com/PP-TSD/sdgen",
	package_dir = {'':'src'},
	packages = find_packages(exclude=['ez_setup', 'examples', 'tests']),
	long_description = read("README.md"),
	classifiers = [],
)
