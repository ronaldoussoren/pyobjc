#
# Run this program from the command line like so:
#
# % python buildapp.py --link build
#
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
