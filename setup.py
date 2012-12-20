#!/usr/bin/env python
"""
Build script.
"""
__docformat__ = 'restructuredtext'

import sys

from setuptools import setup, find_packages

sys.path.insert(0, 'src')

from victims_hash import __version__, __author__


setup(
    name="victims_hash",
    version=__version__,
    description="Fille me in",
    long_description="",
    author=__author__,
    url="https://github.com/victims/victims-hash",
    download_url="https://github.com/victims/victims-hash",

    #license="",

    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,

    #test_suite="",

    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
