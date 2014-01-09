"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="CocoaDrawingShell",
    app=["main.py"],
    data_files=["English.lproj"],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-Quartz",
    ]
)
