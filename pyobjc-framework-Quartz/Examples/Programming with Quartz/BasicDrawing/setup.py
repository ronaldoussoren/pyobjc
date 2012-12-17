"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app
import os

setup(
    name='BasicDrawing',
    app=["main.py"],
    data_files=["English.lproj"] + [ os.path.join('GraphicsFiles', fn) for fn in os.listdir('GraphicsFiles') ],
)
