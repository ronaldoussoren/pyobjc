"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    name="Grady",
    app=["main.py"],
    data_files=["English.lproj"],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
