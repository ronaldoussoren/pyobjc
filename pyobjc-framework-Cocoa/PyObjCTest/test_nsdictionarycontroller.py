import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSDictionaryControllerHelper(AppKit.NSObject):
    def isExplicitlyIncluded(self):
        return 1


class TestNSDictionaryController(TestCase):
    def testProtocols(self):
        self.assertResultIsBOOL(TestNSDictionaryControllerHelper.isExplicitlyIncluded)
