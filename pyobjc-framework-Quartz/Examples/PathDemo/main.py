from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("MainMenu")

import DemoView
import PathDemoController

AppHelper.runEventLoop()
