"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    app=["RoundTransparentWindow.py"],
    data_files=["MainMenu.nib", "circle.tif", "pentagram.tif" ],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
