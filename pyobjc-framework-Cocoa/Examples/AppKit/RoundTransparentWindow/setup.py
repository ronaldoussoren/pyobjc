"""
Script for building the example.

Usage:
    python setup.py py2app
""" 
from distutils.core import setup
import py2app

setup(
    app=["RoundTransparentWindow.py"],
    data_files=["MainMenu.nib", "circle.tif", "pentagram.tif" ],
)
