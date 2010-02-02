from Foundation import *
import objc

from PyObjCTools.TestSupport import *


class TestNSLockProtocols (TestCase):

    def testLockIsLock(self):
        # Test for bug #1735937
        lock = NSLock.alloc().init()
        self.assert_(lock.conformsToProtocol_(objc.protocolNamed("NSLocking")))

        self.assert_(lock.conformsToProtocol_(protocols.NSLocking))

    def testMethods(self):
        self.assertResultIsBOOL(NSLock.tryLock)
        self.assertResultIsBOOL(NSLock.lockBeforeDate_)

        self.assertResultIsBOOL(NSConditionLock.tryLock)
        self.assertResultIsBOOL(NSConditionLock.tryLockWhenCondition_)
        self.assertResultIsBOOL(NSConditionLock.lockBeforeDate_)
        self.assertResultIsBOOL(NSConditionLock.lockWhenCondition_beforeDate_)

        self.assertResultIsBOOL(NSRecursiveLock.tryLock)
        self.assertResultIsBOOL(NSRecursiveLock.lockBeforeDate_)

        self.assertResultIsBOOL(NSCondition.waitUntilDate_)


if __name__ == "__main__":
    main()
