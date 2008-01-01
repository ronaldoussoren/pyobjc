from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("MainMenu")

import MyView

AppHelper.runEventLoop()
