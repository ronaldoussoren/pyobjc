"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="PyChart",
    app=["main.py"],
    data_files=[
        "English.lproj",
        "Chart.qtz"
    ],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-Quartz",
    ]
)
