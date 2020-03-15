import objc
import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSLockProtocols(TestCase):
    def testLockIsLock(self):
        # Test for bug #1735937
        lock = Foundation.NSLock.alloc().init()
        self.assertTrue(lock.conformsToProtocol_(objc.protocolNamed("NSLocking")))

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSLock.tryLock)
        self.assertResultIsBOOL(Foundation.NSLock.lockBeforeDate_)

        self.assertResultIsBOOL(Foundation.NSConditionLock.tryLock)
        self.assertResultIsBOOL(Foundation.NSConditionLock.tryLockWhenCondition_)
        self.assertResultIsBOOL(Foundation.NSConditionLock.lockBeforeDate_)
        self.assertResultIsBOOL(
            Foundation.NSConditionLock.lockWhenCondition_beforeDate_
        )

        self.assertResultIsBOOL(Foundation.NSRecursiveLock.tryLock)
        self.assertResultIsBOOL(Foundation.NSRecursiveLock.lockBeforeDate_)

        self.assertResultIsBOOL(Foundation.NSCondition.waitUntilDate_)
