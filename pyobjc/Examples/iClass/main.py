"""
"""
import time
print time.localtime(), "iClass Startup"
from AppKit import NSApplicationMain, NibClassBuilder
print time.localtime(), "import AppKit"
from Foundation import NSBundle
print time.localtime(), "import Foundation"
import sys
print time.localtime(), "import sys"
import os
print time.localtime(), "import os"

NibClassBuilder.extractClasses('MainMenu.nib')
print time.localtime(), "NIBClassBuilder.extractCls"

import datasource
print time.localtime(), "import datasource"

NSApplicationMain(sys.argv)
print time.localtime(), "NSAppMain done"
