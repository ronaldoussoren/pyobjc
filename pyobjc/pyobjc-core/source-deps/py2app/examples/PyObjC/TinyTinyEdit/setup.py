"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    CFBundleDocumentTypes=[
        dict(
            CFBundleTypeExtensions=["txt", "text", "*"],
            CFBundleTypeName="Text File",
            CFBundleTypeRole="Editor",
            NSDocumentClass="TinyTinyDocument",
        ),
    ],
)

setup(
    data_files=['MainMenu.nib', 'TinyTinyDocument.nib'],
    app=[
        dict(script="TinyTinyEdit.py", plist=plist),
    ],
)
