import sys
from PyObjCTools import AppHelper

from twisted.internet.threadedselectreactor import install
reactor = install()

# import classes required to start application
import WSTApplicationDelegateClass
import WSTConnectionWindowControllerClass

# pass control to the AppKit
AppHelper.runEventLoop()
