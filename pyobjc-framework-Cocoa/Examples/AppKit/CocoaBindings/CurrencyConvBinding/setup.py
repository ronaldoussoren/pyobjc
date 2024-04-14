"""
Script for building the example:

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

plist = {
    "CFBundleDocumentTypes": [
        {
            "CFBundleTypeExtensions": ["CurrencyConvBinding", "*"],
            "CFBundleTypeName": "CurrencyConvBinding File",
            "CFBundleTypeRole": "Editor",
            "NSDocumentClass": "CurrencyConvBindingDocument",
        }
    ]
}

setup(
    name="CurrencyConvBinding",
    app=["CurrencyConvBinding.py"],
    data_files=["English.lproj"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "pyobjc-framework-Cocoa"],
)
