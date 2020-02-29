import sys

import AppKit
import Foundation

# import pyobjc
import objc

# import classes required to start application
import WSTApplicationDelegateClass
import WSTConnectionWindowControllerClass

# pass control to the AppKit
sys.exit(AppKit.NSApplicationMain(sys.argv))
