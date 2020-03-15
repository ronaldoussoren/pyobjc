import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSDistributedLock(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSDistributedLock.tryLock)
