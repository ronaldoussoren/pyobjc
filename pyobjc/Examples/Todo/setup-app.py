#!/usr/bin/env pythonw
"""
Python script for building the applet.
"""

import objc.builder
import os

images = [ os.path.join('Images', fn) for fn in os.listdir('Images') if fn.lower().endswith('.tiff') ]
icons = [ os.path.join('Icons', fn) for fn in os.listdir('Icons') if fn.lower().endswith('.icns') ]

objc.builder.build_applet(
	app_name= 'ToDo',
	main_py = 'main.py',
	extra_src = [ fn for fn in os.listdir('.') if fn.endswith('.py') and fn != 'main.py' ],
	info_plist = 'Info.plist',
	raw=False,
	extra_files = ['English.lproj' ] + images + icons 
)
