#!/usr/bin/env pythonw
"""
Python script for building the applet.
"""

import objc.builder

objc.builder.build_applet(
	app_name= 'iClass',
	main_py = 'main.py',
	raw = True,
	extra_src = ['datasource.py', 'nibwrapper.py'],
	extra_files = ['English.lproj'])
