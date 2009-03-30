from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSDistributedNotificationCenter (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSLocalNotificationCenterType, unicode))

        self.assertEquals(NSNotificationSuspensionBehaviorDrop, 1)
        self.assertEquals(NSNotificationSuspensionBehaviorCoalesce, 2)
        self.assertEquals(NSNotificationSuspensionBehaviorHold, 3)
        self.assertEquals(NSNotificationSuspensionBehaviorDeliverImmediately, 4)

        self.assertEquals(NSNotificationDeliverImmediately, 1)
        self.assertEquals(NSNotificationPostToAllSessions, 2)

    def testMethods(self):
        self.failUnlessArgIsSEL(NSDistributedNotificationCenter.addObserver_selector_name_object_suspensionBehavior_, 1, 'v@:@')
        self.failUnlessArgIsSEL(NSDistributedNotificationCenter.addObserver_selector_name_object_, 1, 'v@:@')

        self.failUnlessArgIsBOOL(NSDistributedNotificationCenter.postNotificationName_object_userInfo_deliverImmediately_, 3)
        self.failUnlessArgIsBOOL(NSDistributedNotificationCenter.setSuspended_, 0)
        self.failUnlessResultIsBOOL(NSDistributedNotificationCenter.suspended)

if __name__ == "__main__":
    main()
