from bundlebuilder import buildapp

buildapp(
    mainprogram = "PackMan.py",
    resources = ["MainMenu.nib"],
    includeModules=['newclient'],
    symlink = True,
    nibname = "MainMenu"
)