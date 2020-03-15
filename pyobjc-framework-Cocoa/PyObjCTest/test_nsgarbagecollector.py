import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSGarbageCollector(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSGarbageCollector.isCollecting)
        self.assertResultIsBOOL(Foundation.NSGarbageCollector.isEnabled)
