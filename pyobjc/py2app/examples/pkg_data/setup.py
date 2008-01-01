"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    app=['use_testpkg.py'],
    options=dict(py2app=dict(
        includes=['testpkg.*'],
        packages=['testpkg'],
    )),
    setup_requires=["py2app"],
)
