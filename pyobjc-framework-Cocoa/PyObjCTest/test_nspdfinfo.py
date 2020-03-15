import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSPDFInfo(TestCase):
    @min_os_level("10.9")
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSPDFInfo.isFileExtensionHidden)
        self.assertArgIsBOOL(AppKit.NSPDFInfo.setFileExtensionHidden_, 0)
