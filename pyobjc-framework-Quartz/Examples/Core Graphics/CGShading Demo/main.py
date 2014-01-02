from PyObjCTools import AppHelper

import MyQuartzView

import objc; objc.setVerbose(True)

#AppHelper.runEventLoop()
import AppKit, sys
AppKit.NSApplicationMain(sys.argv)
