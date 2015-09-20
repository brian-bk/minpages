#!/usr/bin/env python
from __future__ import print_function

from glob import glob
from setuptools import setup, find_packages

setup(
        name = 'minpages',
        version = '0.1',
        description = 'An abbreviated man-pages', 
        long_description = """\
                Hello!""",
        author = 'Brian Kleszyk',
        author_email = 'bkleszyk@gmail.com',
        packages = find_packages(),
        data_files=[('minpages/pages',glob('pages/*'))],
        entry_points = {
            'console_scripts': ['min = minpages.min:main']
        },
        install_requires=['click']
)


