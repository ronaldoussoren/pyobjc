from PyObjCTools.TestSupport import TestCase
import VideoSubscriberAccount


class TestVSSubscription(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(VideoSubscriberAccount.VSSubscriptionAccessLevel)

    def testConstants(self):
        self.assertEqual(VideoSubscriberAccount.VSSubscriptionAccessLevelUnknown, 0)
        self.assertEqual(
            VideoSubscriberAccount.VSSubscriptionAccessLevelFreeWithAccount, 1
        )
        self.assertEqual(VideoSubscriberAccount.VSSubscriptionAccessLevelPaid, 2)

    def testClasses(self):
        VideoSubscriberAccount.VSSubscription
