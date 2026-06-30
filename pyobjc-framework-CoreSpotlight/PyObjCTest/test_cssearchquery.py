from PyObjCTools.TestSupport import TestCase


import CoreSpotlight


class TestCSSearchQuery(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreSpotlight.CSSearchQueryErrorCode)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeUnknown, -2000)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeIndexUnreachable, -2001)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeInvalidQuery, -2002)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeCancelled, -2003)

        self.assertIsEnumType(CoreSpotlight.CSSearchQuerySourceOptions)
        self.assertEqual(CoreSpotlight.CSSearchQuerySourceOptionDefault, 0)
        self.assertEqual(CoreSpotlight.CSSearchQuerySourceOptionAllowMail, 1 << 0)

    def test_constants(self):
        self.assertIsInstance(CoreSpotlight.CSSearchQueryErrorDomain, str)

    def test_methods(self):
        self.assertResultIsBOOL(CoreSpotlight.CSSearchQuery.isCancelled)
        self.assertResultIsBlock(CoreSpotlight.CSSearchQuery.foundItemsHandler, b"v@")
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchQuery.setFoundItemsHandler_, 0, b"v@"
        )
        self.assertResultIsBlock(CoreSpotlight.CSSearchQuery.completionHandler, b"v@")
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchQuery.setCompletionHandler_, 0, b"v@"
        )
