from distutils.core import setup
import py2app

import glob

plist = dict(
    CFBundleShortVersionString='0.1',
    #CFBundleIconFile='EggShell.icns',
    CFBundleGetInfoString='Signatures',
    CFBundleIdentifier='net.sf.pyobjc.signatures',
    CFBundleName='Signatures',
)

setup(
    app=["main.py"],
    data_files=["MainMenu.nib", "tools.py" ],
    options=dict(py2app=dict(plist=plist)),
)
