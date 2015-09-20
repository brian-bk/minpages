#!/usr/bin/env python
from __future__ import print_function

from glob import glob
from os.path import join
from setuptools import setup, find_packages

files = glob('pages/*')
print(files)

setup(
        name = 'minpages',
        version = '0.1',
        description = 'An abbreviated man-pages', 
        long_description = """\
                Hello!""",
        author = 'Brian Kleszyk',
        author_email = 'bkleszyk@gmail.com',
        packages = find_packages(),
        data_files=[('minpages/pages',files)],
        entry_points = {
            'console_scripts': ['min = minpages.min:main']
        },
        install_requires=['click']
)


