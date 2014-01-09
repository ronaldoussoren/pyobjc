"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="Quartz2DBasics.Python",
    app=["main.py"],
    data_files=[
        "English.lproj",
        "GraphicsFiles/ptlobos.tif"
    ],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-Quartz",
    ]
)
