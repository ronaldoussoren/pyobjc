"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = dict(NSMainNibFile="OpenGLDemo")
setup(
    name="OpenGLDemo",
    app=["OpenGLDemo.py"],
    data_files=["OpenGLDemo.nib"],
    options=dict(py2app=dict(plist=plist)),
    setup_requires=[
        "py2app",
        "PyOpenGL",
        "pyobjc-framework-Cocoa",
    ]
)
