from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("MainMenu")

import CIMicroPaintView
import SampleCIView

import objc; objc.setVerbose(True)

AppHelper.runEventLoop()
