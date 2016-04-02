import sys
from PyObjCTools import AppHelper

from twisted.internet import cfreactor
cfreactor.install()

# import classes required to start application
import WSTApplicationDelegateClass
import WSTConnectionWindowControllerClass

# pass control to the AppKit
AppHelper.runEventLoop()
