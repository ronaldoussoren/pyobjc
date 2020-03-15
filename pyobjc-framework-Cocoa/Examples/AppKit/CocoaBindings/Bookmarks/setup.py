"""
Script for building the example:

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = {
    "CFBundleDocumentTypes": [
        {
            "CFBundleTypeExtensions": ["Bookmarks", "*"],
            "CFBundleTypeName": "Bookmarks File",
            "CFBundleTypeRole": "Editor",
            "NSDocumentClass": "BookmarksDocument",
        }
    ]
}

setup(
    name="Bookmarks",
    app=["Bookmarks.py"],
    data_files=["English.lproj"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
