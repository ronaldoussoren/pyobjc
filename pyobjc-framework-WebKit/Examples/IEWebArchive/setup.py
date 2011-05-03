"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    CFBundleDocumentTypes = [
        dict(
            CFBundleTypeExtensions=["mht"],
            CFBundleTypeName="Internet Explorer Web Archive",
            CFBundleTypeRole="Editor",
            NSDocumentClass="MHTDocument",
        ),
    ]
)

setup(
    name="MHTViewer",
    app=["main.py"],
    data_files=["MainMenu.nib", "MHTDocument.nib"],
    options=dict(py2app=dict(plist=plist)),
)
