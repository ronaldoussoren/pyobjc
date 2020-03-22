"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

infoPlist = {
    "CFBundleName": "Shell Environment",
    "CFBundleGetInfoString": "Shell Environment Panel",
    "CFBundleVersion": "0.1",
    "CFBundleShortVersionString": "0.1",
    "NSPrefPaneIconLabel": "Shell Environment",
    "NSPrefPaneIconFile": "ShellEnv.icns",
    "NSPrincipalClass": "EnvironmentPane",
    "NSMainNibFile": "EnvironmentPane",
}

setup(
    name="Shell Environment",
    plugin=["ShellEnv.py"],
    data_files=["English.lproj", "Dutch.lproj", "ShellEnv.icns"],
    options={"py2app": {"extension": ".prefPane", "plist": infoPlist}},
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-PreferencePanes",
    ],
)
