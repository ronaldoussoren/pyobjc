"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    name="PyObjC Launcher",
    app=["PyObjCLauncher.py"],
    data_files=["English.lproj"],
    options=dict(
        py2app=dict(
            plist="Info.plist",
        )
    ),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
