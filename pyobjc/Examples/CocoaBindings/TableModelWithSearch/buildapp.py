"""
Script for building the example, alternative for the Xcode project

Usage:
        python buildapp.py build
"""
from bundlebuilder import buildapp

buildapp(
        name = "TableModelWithSearch",
	mainprogram = "__main__.py",
	resources = [
                "English.lproj", 
                "FilteringArrayController.py",
                "TableModelWithSearchAppDelegate.py",
                "ToolbarCreator.py",
            ],
	nibname = "MainMenu",
)
