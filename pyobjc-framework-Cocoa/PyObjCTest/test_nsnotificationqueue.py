import Foundation
from PyObjCTools.TestSupport import TestCase


class TestNSNotificationQueue(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSNotificationCoalescing)
        self.assertIsEnumType(Foundation.NSPostingStyle)

    def testConstants(self):
        self.assertEqual(Foundation.NSPostWhenIdle, 1)
        self.assertEqual(Foundation.NSPostASAP, 2)
        self.assertEqual(Foundation.NSPostNow, 3)

        self.assertEqual(Foundation.NSNotificationNoCoalescing, 0)
        self.assertEqual(Foundation.NSNotificationCoalescingOnName, 1)
        self.assertEqual(Foundation.NSNotificationCoalescingOnSender, 2)
