"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    app=["main.py"],
    data_files=["English.lproj"],
    setup_requires=["py2app"],
    options=dict(py2app=dict(plist=dict(
        CFBundleName='iClass',
    ))),
)
