from PyObjCTools.TestSupport import *

from Foundation import *


class TestNSNotificationQueue (TestCase):
    def testConstants(self):
        self.assertEqual(NSPostWhenIdle, 1)
        self.assertEqual(NSPostASAP, 2)
        self.assertEqual(NSPostNow, 3)

        self.assertEqual(NSNotificationNoCoalescing, 0)
        self.assertEqual(NSNotificationCoalescingOnName, 1)
        self.assertEqual(NSNotificationCoalescingOnSender, 2)


if __name__ == "__main__":
    main()
