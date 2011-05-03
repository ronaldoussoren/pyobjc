"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

setup(
    name='CIHazeFilterSample',
    app=["main.py"],
    data_files=["English.lproj", 'MyHazeRemoval.cikernel', 'CraterLake.jpg'],
)

