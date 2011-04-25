"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from setuptools import setup
import sys

infoPlist = dict(
    CFBundleName='Shell Environment',
    #CFBundleIconFile='ShellEnv.icns',
    CFBundleGetInfoString='Shell Environment Panel',
    CFBundleVersion='0.1',
    CFBundleShortVersionString = '0.1',
    NSPrefPaneIconLabel='Shell Environment',
    NSPrefPaneIconFile='ShellEnv.icns',
    NSPrincipalClass='EnvironmentPane',
    NSMainNibFile='EnvironmentPane',
)

setup_args = {}
if sys.version_info[0] == 3:
    setup_args['use_2to3'] = 1

setup(
    name="Shell Environment",
    plugin=['ShellEnv.py'],
    data_files=["English.lproj", "Dutch.lproj", "ShellEnv.icns"],
    options=dict(py2app=dict(
        extension=".prefPane",
        plist=infoPlist,
    )),
    **setup_args
)
