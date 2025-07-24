from PyObjCTools.TestSupport import TestCase
import VideoSubscriberAccount


class TestVSAutoSignInAuthorization(TestCase):
    def test_constants(self):
        self.assertIsEnumType(VideoSubscriberAccount.VSAutoSignInAuthorization)
        self.assertEqual(
            VideoSubscriberAccount.VSAutoSignInAuthorizationNotDetermined, 0
        )
        self.assertEqual(VideoSubscriberAccount.VSAutoSignInAuthorizationGranted, 1)
        self.assertEqual(VideoSubscriberAccount.VSAutoSignInAuthorizationDenied, 2)
