import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSDistributedLock(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSDistributedLock.tryLock)
