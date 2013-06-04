"""
Script for building the example.

Usage:
    python setup.py py2app

To use this copy dist/PyAddressLabel.plugin to the plugin directory:
   $ mv dist/PyAddressLabel.plugin \
           ~/Library/Address\ Book\ Plug-Ins/PyAddressLabel.plugin
"""
from setuptools import setup

infoPlist = dict(
    CFBundleName="PyAddressLabel",
    CFBundleGetInfoString="Silly PopUp for AddressBook",
    CFBundleVersion="0.1",
    CFBundleShortVersionString="0.1",
    NSPrincipalClass="PyAddressLabelDelegate",
)

setup(
    name="PyAddressLabel",
    plugin=["plugin.py"],
    data_files=[],
    setup_request=[
        "py2app",
        "pyobjc-framework-AddressBook",
        "pyobjc-framework-Cocoa",
    ],
    options=dict(
        py2app=dict(
            extension=".bundle",
            plist=infoPlist,
        )
    ),
)
