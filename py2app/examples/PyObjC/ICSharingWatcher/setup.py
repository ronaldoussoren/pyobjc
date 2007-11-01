"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup

setup(
    data_files=['MainMenu.nib'],
    app=['ICSharingWatcher.py'],
    install_requires=["pyobjc"],
    setup_requires=["py2app"],
)
