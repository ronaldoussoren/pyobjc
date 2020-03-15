import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSColorList(TestCase):
    def testConstants(self):
        self.assertIsInstance(AppKit.NSColorListDidChangeNotification, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSColorList.isEditable)
        self.assertResultIsBOOL(AppKit.NSColorList.writeToFile_)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(AppKit.NSColorList.writeToURL_error_)
        self.assertArgIsOut(AppKit.NSColorList.writeToURL_error_, 1)
