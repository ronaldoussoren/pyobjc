#! /usr/local/python

import os

from bundlebuilder import buildapp

src = [ fn for fn in os.listdir('.') if fn.endswith('.py') and fn not in ('Main.py', 'buildapp.py') ]

buildapp(
	name = "FieldGraph",
	mainprogram = "Main.py",
	resources = ["English.lproj", 'CrossCursor.tiff', 'Map.png' ] + src,
	nibname = "MainMenu",
)
