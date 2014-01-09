"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    app=["Main.py"],
    data_files=[
        "English.lproj",
        "Preferences.png",
        "Reload.png",
        "WST.png"
    ],
    options=dict(py2app=dict(
        iconfile="WST.icns",
        plist=dict(CFBundleName="Web Services Tool"),
    )),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
    ]
)
