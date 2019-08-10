"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="AutoSample",
    app=["main.py"],
    data_files=["English.lproj", "workflows"],
    setup_requires=["pyobjc-framework-Automator", "pyobjc-framework-Cocoa"],
)
