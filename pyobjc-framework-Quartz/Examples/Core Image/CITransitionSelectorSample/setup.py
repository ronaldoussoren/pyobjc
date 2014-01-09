"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

setup(
    name="CITransitionSelectorSample",
    app=["main.py"],
    data_files=[
        "English.lproj",
        "Blank.jpg",
        "Frog.jpg",
        "Mask.jpg",
        "Rose.jpg",
        "Shading.tiff",
    ],
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-Quartz",
    ]
)
