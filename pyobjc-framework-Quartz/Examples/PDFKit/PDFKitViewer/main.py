from PyObjCTools import NibClassBuilder, AppHelper
import objc
objc.setVerbose(True)

NibClassBuilder.extractClasses("MainMenu")
NibClassBuilder.extractClasses("MyDocument")

import MyPDFDocument
import AppDelegate

AppHelper.runEventLoop()
