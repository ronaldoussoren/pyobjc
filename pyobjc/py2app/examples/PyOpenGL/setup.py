"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    app=["lesson5.py"],
    setup_requires=["py2app"],
)
