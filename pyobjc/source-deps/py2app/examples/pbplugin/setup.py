from distutils.core import setup
import py2app

# Copy the hello.pbplugin to:
# ~/Library/Application Support/Apple/Developer Tools/Plug-Ins/
#
# It will just print a bunch of debugging garbage when you start up.

setup(
    plugin = ["hello.py"],
    options = dict(py2app=dict(
        extension='.pbplugin',
    )),
)
