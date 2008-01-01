from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("MainMenu")
NibClassBuilder.extractClasses("TLayerDemo")

import AppDelegate
import Circle
import Extras
import ShadowOffsetView
import TLayerDemo
import TLayerView

import objc; objc.setVerbose(True)

AppHelper.runEventLoop()
