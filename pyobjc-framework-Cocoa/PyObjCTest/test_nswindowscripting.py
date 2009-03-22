from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSWindowScripting (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSWindow.hasCloseBox)
        self.failUnlessResultIsBOOL(NSWindow.hasTitleBar)
        self.failUnlessResultIsBOOL(NSWindow.isFloatingPanel)
        self.failUnlessResultIsBOOL(NSWindow.isMiniaturizable)
        self.failUnlessResultIsBOOL(NSWindow.isModalPanel)
        self.failUnlessResultIsBOOL(NSWindow.isResizable)
        self.failUnlessResultIsBOOL(NSWindow.isZoomable)
        self.failUnlessArgIsBOOL(NSWindow.setIsMiniaturized_, 0)
        self.failUnlessArgIsBOOL(NSWindow.setIsVisible_, 0)
        self.failUnlessArgIsBOOL(NSWindow.setIsZoomed_, 0)

if __name__ == "__main__":
    main()
