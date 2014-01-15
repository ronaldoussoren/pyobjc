"""
Script for building the example.

Usage:
    python3 setup.py py2app
"""
from setuptools import setup


plist = dict(
    NSMainNibFile="MainMenu",
    CFBundleDocumentTypes=[
        dict(
            CFBundleTypeExtensions=["binary"],
            CFBundleTypeMIMETypes=["application/octect-stream"],
            CFBundleTypeName="Binary",
            CFBundleTypeRole="Editor",
            LSTypeIsPackage=False,
            NSDocumentClass="MyDocument",
            NSPersistentStoreTypeKey="Binary",
        ),
        dict(
            CFBundleTypeExtensions=["sql"],
            CFBundleTypeMIMETypes=["application/octect-stream"],
            CFBundleTypeName="SQL",
            CFBundleTypeRole="Editor",
            LSTypeIsPackage=False,
            NSDocumentClass="MyDocument",
            NSPersistentStoreTypeKey="SQLite",
        ),
        dict(
            CFBundleTypeExtensions=["xml"],
            CFBundleTypeMIMETypes=["text/xml"],
            CFBundleTypeName="XML",
            CFBundleOSTypes=["????"],
            CFBundleTypeRole="Editor",
            LSTypeIsPackage=False,
            NSDocumentClass="MyDocument",
            NSPersistentStoreTypeKey="XML",
        ),
    ],
)

setup(
    name="PyOutlineEdit",
    app=["main.py"],
    data_files=["English.lproj"],
    options=dict(py2app=dict(
        plist=plist,
        datamodels=["MyDocument"],
    )),
    setup_requires=[
        "py2app",
        "pyobjc-framework-Cocoa",
        "pyobjc-framework-CoreData",
    ]
)
