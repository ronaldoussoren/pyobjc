import sys
from Foundation import NSObject
from AppKit import NSApplicationMain
from PyObjCTools import NibClassBuilder
from objc import *

NibClassBuilder.extractClasses('MainMenu.nib')

from CGraphController import *

sys.exit(NSApplicationMain(sys.argv))
