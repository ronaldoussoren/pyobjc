import sys

import AppKit

# import classes required to start application
import WSTApplicationDelegateClass  # noqa F401
import WSTConnectionWindowControllerClass  # noqa F401

# pass control to the AppKit
sys.exit(AppKit.NSApplicationMain(sys.argv))
