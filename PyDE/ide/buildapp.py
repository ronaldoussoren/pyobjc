import os

from bundlebuilder import buildapp
from plistlib import Plist, Dict

plist = Plist(
        CFBundleDocumentTypes = [
            Dict(
                CFBundleTypeExtensions = [ "py", "pyw" ],
                CFBundleTypeName = "Python File",
                CFBundleTypeRole = "Editor",
                NSDocumentClass = "PyDEPythonDocument",
            ),
        ],
    )

buildapp(
        name = "PyDE",
        mainprogram = "main.py",
        resources = [ 
            os.path.join("Resources", x) 
                for x in os.listdir("Resources")
                if x != 'CVS' ] + [ 'pythonfile.py', 'PyDETextView.py', 'PyFontify.py'],
        nibname = "MainMenu.nib",
        plist = plist,
    )
