from distutils.core import setup
import py2app

plist = dict(
    CFBundleDocumentTypes = [
        dict(
            CFBundleTypeExtensions = ["txt", "text", "*"],
            CFBundleTypeName = "Text File",
            CFBundleTypeRole = "Editor",
            NSDocumentClass = "TinyTinyDocument",
        ),
    ]
)


setup(
    app = ["TinyTinyEdit.py"],
    data_files = ["MainMenu.nib", "TinyTinyDocument.nib"],
    options = dict(py2app=dict(plist=plist)),
)
