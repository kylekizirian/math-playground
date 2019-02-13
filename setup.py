#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import math_playground

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'math_playground'
DESCRIPTION = 'Playground for math related code.'
URL = 'https://github.com/kylekizirian/math-playground'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = math_playground.__version__

# What packages are required for this module to be executed?
REQUIRED = []


# Where the magic happens:
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT'
)