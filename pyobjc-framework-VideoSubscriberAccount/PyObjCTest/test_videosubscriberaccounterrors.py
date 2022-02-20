from PyObjCTools.TestSupport import TestCase
import VideoSubscriberAccount


class TestVideoSubscriberAccountErrors(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(VideoSubscriberAccount.VSErrorCode)

    def testConstants(self):
        self.assertIsInstance(VideoSubscriberAccount.VSErrorDomain, str)
        self.assertIsInstance(VideoSubscriberAccount.VSErrorInfoKeySAMLResponse, str)
        self.assertIsInstance(
            VideoSubscriberAccount.VSErrorInfoKeySAMLResponseStatus, str
        )
        self.assertIsInstance(
            VideoSubscriberAccount.VSErrorInfoKeyAccountProviderResponse, str
        )
        self.assertIsInstance(
            VideoSubscriberAccount.VSErrorInfoKeyUnsupportedProviderIdentifier, str
        )

        self.assertEqual(VideoSubscriberAccount.VSErrorCodeAccessNotGranted, 0)
        self.assertEqual(VideoSubscriberAccount.VSErrorCodeUnsupportedProvider, 1)
        self.assertEqual(VideoSubscriberAccount.VSErrorCodeUserCancelled, 2)
        self.assertEqual(
            VideoSubscriberAccount.VSErrorCodeServiceTemporarilyUnavailable, 3
        )
        self.assertEqual(VideoSubscriberAccount.VSErrorCodeProviderRejected, 4)
        self.assertEqual(VideoSubscriberAccount.VSErrorCodeInvalidVerificationToken, 5)
        self.assertEqual(VideoSubscriberAccount.VSErrorCodeRejected, 6)
        self.assertEqual(VideoSubscriberAccount.VSErrorCodeUnsupported, 7)
