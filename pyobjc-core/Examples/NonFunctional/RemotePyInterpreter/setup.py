"""
Script for building the example.

Usage:
    python setup.py py2app
"""
from distutils.core import setup
import py2app

plist = dict(
    CFBundleIdentifier=u'net.sf.pyobjc.RemotePyInterpreter',
    CFBundleDocumentTypes=[
        dict(
            CFBundleTypeExtensions=[
                u'RemotePyInterpreter',
                u'*',
            ],
            CFBundleTypeName=u'RemotePyInterpreter Session',
            CFBundleTypeRole=u'Editor',
            NSDocumentClass=u'RemotePyInterpreterDocument',
        ),
    ],
)

REMOTE_REQUIREMENTS = ['tcpinterpreter', 'netrepr', 'remote_console', 'remote_pipe', 'remote_bootstrap']
DATA_FILES = ['English.lproj'] + [(s + '.py') for s in REMOTE_REQUIREMENTS]

setup(
    app=["RemotePyInterpreter.py"],
    data_files=DATA_FILES,
    options=dict(py2app=dict(plist=plist)),
)
