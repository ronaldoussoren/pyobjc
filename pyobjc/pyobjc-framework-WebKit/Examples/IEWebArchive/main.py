import MHTDocument
import objc; objc.setVerbose(1)

# XXX: Workaround for an issue
# in py2app: this module is required
# but isn't found by py2app by default.
import email.iterators

from PyObjCTools import AppHelper

AppHelper.runEventLoop()
