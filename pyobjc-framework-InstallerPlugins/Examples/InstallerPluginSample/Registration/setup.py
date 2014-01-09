"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup

plist = dict(
    InstallerSectionTitle="PyRegistration",
    NSMainNibFile="Registration",
    NSPrincipalClass="InstallerSection",
    CFBundleIdentifier="com.MyCompany.Installer.example.Registration",
)

setup(
    name="Registration",
    plugin=["RegistrationPane.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        extension=".bundle",
        plist=plist,
    )),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-InstallerPlugins",
    ]

)
