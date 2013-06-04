"""
Script for building the example, alternative to the Xcode project

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    name="TableModelWithSearch",
    app=["main.py"],
    data_files=["English.lproj"],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
