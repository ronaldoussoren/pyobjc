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

if __name__ == "__main__":
    main()
