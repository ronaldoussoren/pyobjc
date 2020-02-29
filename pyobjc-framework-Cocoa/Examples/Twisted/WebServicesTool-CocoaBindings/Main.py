# import classes required to start application
import WSTApplicationDelegateClass
import WSTConnectionWindowControllerClass
from PyObjCTools import AppHelper
from twisted.internet import cfreactor

cfreactor.install()


# pass control to the AppKit
AppHelper.runEventLoop()
