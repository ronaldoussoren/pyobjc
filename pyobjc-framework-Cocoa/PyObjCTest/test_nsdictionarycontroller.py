import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSDictionaryControllerHelper(AppKit.NSObject):
    def isExplicitlyIncluded(self):
        return 1


class TestNSDictionaryController(TestCase):
    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestNSDictionaryControllerHelper.isExplicitlyIncluded)

    def test_methods(self):
        self.assertResultIsRetained(AppKit.NSDictionaryController.newObject)
