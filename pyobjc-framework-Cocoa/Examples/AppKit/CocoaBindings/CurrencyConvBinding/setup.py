"""
Script for building the example:

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    CFBundleDocumentTypes=[
        dict(
            CFBundleTypeExtensions=[
                'CurrencyConvBinding',
                '*',
            ],
            CFBundleTypeName='CurrencyConvBinding File',
            CFBundleTypeRole='Editor',
            NSDocumentClass='CurrencyConvBindingDocument',
        ),
    ],
)

setup(
    app=["CurrencyConvBinding.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        plist=plist,
    )),
)
