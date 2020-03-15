import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSPortMessage(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSPortMessage.sendBeforeDate_)
