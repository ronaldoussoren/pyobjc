from bundlebuilder import buildapp

buildapp(
    mainprogram = "PackMan.py",
    resources = ["MainMenu.nib"],
    includeModules=['newclient', 'newpimp'],
    symlink = True,
    nibname = "MainMenu"
)
