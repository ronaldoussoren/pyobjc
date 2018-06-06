from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import VideoSubscriberAccount

    class TestVSSubscription (TestCase):
        def testConstants(self):
            self.assertEqual(VideoSubscriberAccount.VSSubscriptionAccessLevelUnknown, 0)
            self.assertEqual(VideoSubscriberAccount.VSSubscriptionAccessLevelFreeWithAccount, 1)
            self.assertEqual(VideoSubscriberAccount.VSSubscriptionAccessLevelPaid, 2)

        def testClasses(self):
            VideoSubscriberAccount.VSSubscription


if __name__ == "__main__":
    main()
