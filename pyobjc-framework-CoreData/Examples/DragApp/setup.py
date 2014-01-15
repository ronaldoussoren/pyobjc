"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="DragApp",
    app=["main.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        datamodels=["DragApp_DataModel.xcdatamodel"],
    )),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-CoreData",
    ]
)
