import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSWindowScripting(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSWindow.hasCloseBox)
        self.assertResultIsBOOL(AppKit.NSWindow.hasTitleBar)
        self.assertResultIsBOOL(AppKit.NSWindow.isFloatingPanel)
        self.assertResultIsBOOL(AppKit.NSWindow.isMiniaturizable)
        self.assertResultIsBOOL(AppKit.NSWindow.isModalPanel)
        self.assertResultIsBOOL(AppKit.NSWindow.isResizable)
        self.assertResultIsBOOL(AppKit.NSWindow.isZoomable)
        self.assertArgIsBOOL(AppKit.NSWindow.setIsMiniaturized_, 0)
        self.assertArgIsBOOL(AppKit.NSWindow.setIsVisible_, 0)
        self.assertArgIsBOOL(AppKit.NSWindow.setIsZoomed_, 0)
