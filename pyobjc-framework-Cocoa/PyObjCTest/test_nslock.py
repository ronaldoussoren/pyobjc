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
        self.failUnlessResultIsBOOL(NSLock.tryLock)
        self.failUnlessResultIsBOOL(NSLock.lockBeforeDate_)

        self.failUnlessResultIsBOOL(NSConditionLock.tryLock)
        self.failUnlessResultIsBOOL(NSConditionLock.tryLockWhenCondition_)
        self.failUnlessResultIsBOOL(NSConditionLock.lockBeforeDate_)
        self.failUnlessResultIsBOOL(NSConditionLock.lockWhenCondition_beforeDate_)

        self.failUnlessResultIsBOOL(NSRecursiveLock.tryLock)
        self.failUnlessResultIsBOOL(NSRecursiveLock.lockBeforeDate_)

        self.failUnlessResultIsBOOL(NSCondition.waitUntilDate_)


if __name__ == "__main__":
    main()
