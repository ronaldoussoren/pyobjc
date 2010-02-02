from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSWindowScripting (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSWindow.hasCloseBox)
        self.assertResultIsBOOL(NSWindow.hasTitleBar)
        self.assertResultIsBOOL(NSWindow.isFloatingPanel)
        self.assertResultIsBOOL(NSWindow.isMiniaturizable)
        self.assertResultIsBOOL(NSWindow.isModalPanel)
        self.assertResultIsBOOL(NSWindow.isResizable)
        self.assertResultIsBOOL(NSWindow.isZoomable)
        self.assertArgIsBOOL(NSWindow.setIsMiniaturized_, 0)
        self.assertArgIsBOOL(NSWindow.setIsVisible_, 0)
        self.assertArgIsBOOL(NSWindow.setIsZoomed_, 0)

if __name__ == "__main__":
    main()
