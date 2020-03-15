"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = {"NSMainNibFile": "OpenGLDemo"}
setup(
    name="OpenGLDemo",
    app=["OpenGLDemo.py"],
    data_files=["OpenGLDemo.nib"],
    options={"py2app": {"plist": plist}},
    setup_requires=["py2app", "PyOpenGL", "pyobjc-framework-Cocoa"],
)
