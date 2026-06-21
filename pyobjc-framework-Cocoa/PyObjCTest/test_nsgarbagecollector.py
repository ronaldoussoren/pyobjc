import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSGarbageCollector(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSGarbageCollector.isCollecting)
        self.assertResultIsBOOL(Foundation.NSGarbageCollector.isEnabled)
