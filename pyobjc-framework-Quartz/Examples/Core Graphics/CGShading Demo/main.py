from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("MainMenu")

import MyQuartzView

import objc; objc.setVerbose(True)

#AppHelper.runEventLoop()
import AppKit, sys
AppKit.NSApplicationMain(sys.argv)
