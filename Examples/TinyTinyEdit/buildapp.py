from bundlebuilder import buildapp
from plistlib import Plist, Dict


plist = Plist(
    CFBundleDocumentTypes = [
        Dict(
            CFBundleTypeExtensions = ["txt", "text", "*"],
            CFBundleTypeName = "Text File",
            CFBundleTypeRole = "Editor",
            NSDocumentClass = "TinyTinyDocument",
        ),
    ]
)


buildapp(
    mainprogram = "TinyTinyEdit.py",
    resources = ["MainMenu.nib", "TinyTinyDocument.nib"],
    nibname = "MainMenu",
    plist = plist,
)
