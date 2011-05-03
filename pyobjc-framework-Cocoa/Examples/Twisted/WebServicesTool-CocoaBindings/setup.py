"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

setup(
    name="WebServices Tool (CoreData)",
    app=["Main.py"],
    data_files=["English.lproj", "Preferences.png", "Reload.png", "WST.png"],
    options=dict(py2app=dict(
        iconfile="WST.icns",
    )),
)
