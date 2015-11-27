from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSDistributedNotificationCenter (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSLocalNotificationCenterType, unicode)
        self.assertEqual(NSNotificationSuspensionBehaviorDrop, 1)
        self.assertEqual(NSNotificationSuspensionBehaviorCoalesce, 2)
        self.assertEqual(NSNotificationSuspensionBehaviorHold, 3)
        self.assertEqual(NSNotificationSuspensionBehaviorDeliverImmediately, 4)

        self.assertEqual(NSNotificationDeliverImmediately, 1)
        self.assertEqual(NSNotificationPostToAllSessions, 2)

    def testMethods(self):
        self.assertArgIsSEL(NSDistributedNotificationCenter.addObserver_selector_name_object_suspensionBehavior_, 1, b'v@:@')
        self.assertArgIsSEL(NSDistributedNotificationCenter.addObserver_selector_name_object_, 1, b'v@:@')

        self.assertArgIsBOOL(NSDistributedNotificationCenter.postNotificationName_object_userInfo_deliverImmediately_, 3)
        self.assertArgIsBOOL(NSDistributedNotificationCenter.setSuspended_, 0)
        self.assertResultIsBOOL(NSDistributedNotificationCenter.suspended)

if __name__ == "__main__":
    main()
