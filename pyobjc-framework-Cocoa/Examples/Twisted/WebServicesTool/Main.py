# import classes required to start application
import WSTApplicationDelegateClass  # noqa: F401
import WSTConnectionWindowControllerClass  # noqa: F401
from PyObjCTools import AppHelper
from twisted.internet import cfreactor

cfreactor.install()


# pass control to the AppKit
AppHelper.runEventLoop()
