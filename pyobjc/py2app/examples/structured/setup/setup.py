"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    app = ['../python/myapp.py'],
    data_files = ['../data'],
    setup_requires=["py2app"],
)
