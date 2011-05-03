from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("MainMenu")

import MyAppController
import MyView

import objc; objc.setVerbose(True)

AppHelper.runEventLoop()
