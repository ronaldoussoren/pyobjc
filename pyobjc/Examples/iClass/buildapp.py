# These modules are otherwise completely standalone, they don't need any
# Mac- or PyObjC-specific stuff.
#

from bundlebuilder import buildapp

buildapp(
    name = 'iClass',
    mainprogram = "main.py",
    resources = ["English.lproj", "datasource.py" ],
    nibname = "MainMenu",
)
