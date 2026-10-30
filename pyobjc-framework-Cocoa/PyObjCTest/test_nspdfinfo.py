import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSPDFInfo(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSPDFInfo.isFileExtensionHidden)
        self.assertArgIsBOOL(AppKit.NSPDFInfo.setFileExtensionHidden_, 0)
