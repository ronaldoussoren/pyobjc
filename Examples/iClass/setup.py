# These modules are otherwise completely standalone, they don't need any
# Mac- or PyObjC-specific stuff.
#

from distutils.core import setup
import py2app

setup(
    app = ["main.py"],
    data_files = ["English.lproj"],
    options=dict(py2app=dict(plist=dict(
        CFBundleName = 'iClass',
    ))),
)
