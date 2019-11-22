from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2 ** 32:
    import VideoSubscriberAccount

    class TestVideoSubscriberAccountErrors(TestCase):
        def testConstants(self):
            self.assertIsInstance(VideoSubscriberAccount.VSErrorDomain, unicode)
            self.assertIsInstance(
                VideoSubscriberAccount.VSErrorInfoKeySAMLResponse, unicode
            )
            self.assertIsInstance(
                VideoSubscriberAccount.VSErrorInfoKeySAMLResponseStatus, unicode
            )
            self.assertIsInstance(
                VideoSubscriberAccount.VSErrorInfoKeyAccountProviderResponse, unicode
            )
            self.assertIsInstance(
                VideoSubscriberAccount.VSErrorInfoKeyUnsupportedProviderIdentifier,
                unicode,
            )

            self.assertEqual(VideoSubscriberAccount.VSErrorCodeAccessNotGranted, 0)
            self.assertEqual(VideoSubscriberAccount.VSErrorCodeUnsupportedProvider, 1)
            self.assertEqual(VideoSubscriberAccount.VSErrorCodeUserCancelled, 2)
            self.assertEqual(
                VideoSubscriberAccount.VSErrorCodeServiceTemporarilyUnavailable, 3
            )
            self.assertEqual(VideoSubscriberAccount.VSErrorCodeProviderRejected, 4)
            self.assertEqual(
                VideoSubscriberAccount.VSErrorCodeInvalidVerificationToken, 5
            )
            self.assertEqual(VideoSubscriberAccount.VSErrorCodeRejected, 6)


if __name__ == "__main__":
    main()
