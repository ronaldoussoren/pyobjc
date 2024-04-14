"""
Script for building the example:

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

plist = {
    "CFBundleDocumentTypes": [
        {
            "CFBundleTypeExtensions": ["ToDos", "*"],
            "CFBundleTypeName": "ToDos File",
            "CFBundleTypeRole": "Editor",
            "NSDocumentClass": "ToDosDocument",
        }
    ]
}

setup(
    name="ToDos",
    app=["ToDos.py"],
    data_files=["English.lproj"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
