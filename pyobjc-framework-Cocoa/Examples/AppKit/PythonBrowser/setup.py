"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

setup(
    app=["PythonBrowser.py"],
    data_files=["MainMenu.nib", "PythonBrowser.nib"],
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
