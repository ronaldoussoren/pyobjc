"""
"""
import time
from AppKit import NSApplicationMain
from PyObjCTools import NibClassBuilder
from Foundation import NSBundle
import sys
import os

NibClassBuilder.extractClasses('MainMenu.nib')

import datasource

NSApplicationMain(sys.argv)
