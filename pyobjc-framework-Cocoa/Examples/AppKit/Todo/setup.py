"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""

import glob

from setuptools import setup

images = glob.glob("Images/*.tiff")
icons = glob.glob("Icons/*.icns")

plist = {
    "CFBundleShortVersionString": "To Do v1",
    "CFBundleIconFile": "ToDoApp.icns",
    "CFBundleGetInfoString": "To Do v1",
    "CFBundleIdentifier": "net.sf.pyobjc.ToDo",
    "CFBundleDocumentTypes": [
        {
            "CFBundleTypeName": "To Do list",
            "CFBundleTypeRole": "Editor",
            "NSDocumentClass": "ToDoDocument",
            "CFBundleTypeIconFile": "ToDoDoc.icns",
            "CFBundleTypeExtensions": ["ToDo"],
            "CFBundleTypeOSTypes": ["ToDo"],
        }
    ],
    "CFBundleName": "To Do",
}

setup(
    app=["main.py"],
    data_files=["English.lproj"] + images + icons,
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
