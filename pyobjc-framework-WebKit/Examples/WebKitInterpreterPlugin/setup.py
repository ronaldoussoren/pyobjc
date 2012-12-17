"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

MIME = 'application/x-pyobjc-demo-webkitinterpreter'
plist = dict(
    NSPrincipalClass='WebKitInterpreter',
    WebPluginName='WebKit PyInterpreter Plug-In',
    WebPluginDescription='PyObjC demo that embeds a Python interpreter',
    CFBundlePackageType='WBPL',
    WebPluginMIMETypes={
        MIME: dict(
            WebPluginExtensions=['webkitinterpreter'],
            WebPluginTypeDescription='WebKit PyInterpreter',
        ),
    },
)

setup(
    name="WebKitInterpreter",
    plugin = ["WebKitInterpreter.py"],
    options = dict(py2app=dict(plist=plist)),
)
