from distutils.core import setup
import py2app

plist = dict(NSMainNibFile='ClassBrowser')
setup(
    plugin = ["InjectBrowserPlugin.py"],
    data_files = ["ClassBrowser.nib"],
    options = dict(py2app=dict(plist=plist)),
)
