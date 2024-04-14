"""
Script for building the example:

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

plist = {
    "CFBundleDocumentTypes": [
        {
            "CFBundleTypeExtensions": ["GraphicsBindings", "*"],
            "CFBundleTypeName": "GraphicsBindings File",
            "CFBundleTypeRole": "Editor",
            "NSDocumentClass": "GraphicsBindingsDocument",
        }
    ]
}

setup(
    name="GraphicsBinding",
    app=["GraphicsBindings.py"],
    data_files=["English.lproj"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
