"""
Script for building the example.

Usage:
    python setup.py py2app
""" 
from setuptools import setup

setup(
    app=["DragItemAround.py"],
    data_files=["MainMenu.nib"],
    setup_requires=["py2app"],
)
