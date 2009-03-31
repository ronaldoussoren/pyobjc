from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSNotificationQueue (TestCase):
    def testConstants(self):
        self.assertEquals(NSPostWhenIdle, 1)
        self.assertEquals(NSPostASAP, 2)
        self.assertEquals(NSPostNow, 3)

        self.assertEquals(NSNotificationNoCoalescing, 0)
        self.assertEquals(NSNotificationCoalescingOnName, 1)
        self.assertEquals(NSNotificationCoalescingOnSender, 2)


if __name__ == "__main__":
    main()
