"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup
import os

setup(
    name="BasicDrawing",
    app=["main.py"],
    data_files=[
        "English.lproj"
    ] + [
        os.path.join("GraphicsFiles", fn)
        for fn in os.listdir("GraphicsFiles")
    ],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-Quartz",
    ]
)
