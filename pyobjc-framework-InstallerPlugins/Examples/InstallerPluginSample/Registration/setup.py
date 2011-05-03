"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    InstallerSectionTitle="PyRegistration",
    NSMainNibFile='Registration',
    NSPrincipalClass='InstallerSection',
    CFBundleIdentifier='com.MyCompany.Installer.example.Registration',
)

setup(
    name='Registration',
    plugin=['RegistrationPane.py'],
    data_files=['English.lproj'],
    options=dict(py2app=dict(
        extension='.bundle',
        plist=plist,
    )),
)
