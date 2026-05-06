#!/usr/bin/env python
"""
File: setup.py
Author: Keith Tauscher (updated)
Description: Installs distpy.
"""
from setuptools import setup, find_packages

setup(
    name='distpy',
    version='0.1',
    description='Distributions in Python',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'h5py',
    ],
)
