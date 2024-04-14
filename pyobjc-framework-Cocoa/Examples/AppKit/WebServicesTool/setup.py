"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

setup(
    app=["Main.py"],
    data_files=["English.lproj", "Preferences.png", "Reload.png", "WST.png"],
    options={
        "py2app": {
            "iconfile": "WST.icns",
            "plist": {"CFBundleName": "Web Services Tool"},
        }
    },
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
