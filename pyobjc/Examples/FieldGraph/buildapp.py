#
# Successor of setup-app.py. Run this program from the command line like so:
#
# % python buildapp.py build
#
# It depends on two (new) modules from the Python CVS tree:
#    Mac/Lib/bundlebuilder.py
#    Mac/Lib/plistlib.py
# These modules are otherwise completely standalone, they don't need any
# Mac- or PyObjC-specific stuff.
#

from bundlebuilder import buildapp

SRC=[
    'CGraphController.py',
    'CGraphModel.py',
    'CGraphView.py',
    'fieldMath.py',
]

buildapp(
        name = "FieldGraph",
	mainprogram = "Main.py",
	resources = ["English.lproj"] + SRC,
	nibname = "MainMenu",
)
