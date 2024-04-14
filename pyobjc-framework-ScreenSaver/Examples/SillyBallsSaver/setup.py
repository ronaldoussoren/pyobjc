"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

plist = {"NSPrincipalClass": "SillyBalls"}

setup(
    plugin=["SillyBalls.py"],
    data_files=["English.lproj"],
    options={"py2app": {"extension": ".saver", "plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa", "pyobjc-framework-ScreenSaver"],
)
