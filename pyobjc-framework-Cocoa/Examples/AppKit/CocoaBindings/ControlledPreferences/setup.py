"""
Script for building the example:

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    name="ControlledPreferences",
    app=["ControlledPreferences.py"],
    data_files=["English.lproj"],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
