"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app
import os


setup(
    name='DragApp',
    app=["main.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        datamodels=['DragApp_DataModel.xcdatamodel'],
    )),
)
