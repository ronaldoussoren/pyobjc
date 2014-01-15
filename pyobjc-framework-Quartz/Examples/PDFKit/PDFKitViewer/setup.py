"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="PDFKitViewer",
    app=["main.py"],
    data_files=[
        "English.lproj",
        "pdfkitviewer.icns"
    ],
    options=dict(
        py2app=dict(
            plist="Info.plist",
        )),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-Quartz",
    ]
)
