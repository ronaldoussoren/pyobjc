import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSPortMessage(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSPortMessage.sendBeforeDate_)
