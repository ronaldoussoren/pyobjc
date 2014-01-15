"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="CIBevelSample",
    app=["main.py"],
    data_files=[
        "English.lproj",
        "lightball.tiff"
    ]
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-Quartz",
    ]
)
