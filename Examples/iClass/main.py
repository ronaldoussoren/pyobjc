"""
"""
from AppKit import NSApplicationMain, NibClassBuilder
from Foundation import NSBundle
import sys
import os

NibClassBuilder.extractClasses('MainMenu.nib')

import datasource

NSApplicationMain(sys.argv)
