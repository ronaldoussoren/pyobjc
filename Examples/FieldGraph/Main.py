from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses('MainMenu.nib')

import CGraphController

AppHelper.runEventLoop()
