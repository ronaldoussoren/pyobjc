import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSColorWell(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSColorWell.isActive)
        self.assertArgIsBOOL(AppKit.NSColorWell.activate_, 0)
        self.assertResultIsBOOL(AppKit.NSColorWell.isBordered)
        self.assertArgIsBOOL(AppKit.NSColorWell.setBordered_, 0)
