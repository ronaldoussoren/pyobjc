"""
Script for building the example:

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = {
    "CFBundleDocumentTypes": [
        {
            "CFBundleTypeExtensions": ["FilteringController", "*"],
            "CFBundleTypeName": "FilteringController File",
            "CFBundleTypeRole": "Editor",
            "NSDocumentClass": "FilteringControllerDocument",
        }
    ]
}

setup(
    name="FilteringController",
    app=["FilteringController.py"],
    data_files=["English.lproj"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
