"""
Script for building the example, alternative for the Xcode project.

Usage:
    python buildapp.py build
"""
from bundlebuilder import buildapp

buildapp(
        name = "TableModel",
	mainprogram = "__main__.py",
	resources = ["English.lproj", "TableModelAppDelegate.py" ],
	nibname = "MainMenu",
)
