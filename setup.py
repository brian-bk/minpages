#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
        name = 'minpages',
        version = '0.1',
        description = 'An abbreviated man-pages', 
        long_description = """\
                Hello!""",
        author = 'Brian Kleszyk',
        author_email = 'bkleszyk@gmail.com',
        packages = find_packages(exclude='test'),
        entry_points = {
            'console_scripts': ['min = minpages.min:main']
        },
        install_requires=['click']
)


