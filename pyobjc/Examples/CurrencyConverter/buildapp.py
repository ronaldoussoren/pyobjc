#
# Script for building the .app bundle.
#
# Usage:
#   python buildapp.py build
#
from bundlebuilder import buildapp

buildapp(
    mainprogram = "CurrencyConverter.py",
    resources = ["English.lproj" ],
    nibname = "MainMenu",
)
