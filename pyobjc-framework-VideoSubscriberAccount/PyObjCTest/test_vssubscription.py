from PyObjCTools.TestSupport import TestCase
import VideoSubscriberAccount


class TestVSSubscription(TestCase):
    def test_enums(self):
        self.assertIsEnumType(VideoSubscriberAccount.VSSubscriptionAccessLevel)
        self.assertEqual(VideoSubscriberAccount.VSSubscriptionAccessLevelUnknown, 0)
        self.assertEqual(
            VideoSubscriberAccount.VSSubscriptionAccessLevelFreeWithAccount, 1
        )
        self.assertEqual(VideoSubscriberAccount.VSSubscriptionAccessLevelPaid, 2)
