#!/usr/bin/env pythonw
"""
Python script for building the applet.
"""

import objc.builder

objc.builder.build_applet(
	app_name= 'CurrencyConverterPY',
	main_py = 'CurrencyConverter.py',
	extra_files = ['English.lproj/MainMenu.nib'])
# NOTE: We'd like to use just 'English.lproj', but buildtools.py gets 
# confused by that....
