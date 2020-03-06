import AppController  # noqa: F401
import CalController  # noqa: F401
import objc
from PyObjCTools import AppHelper

objc.setVerbose(True)


AppHelper.runEventLoop()
