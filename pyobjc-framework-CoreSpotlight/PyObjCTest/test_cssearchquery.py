from PyObjCTools.TestSupport import TestCase


import CoreSpotlight


class TestCSSearchQuery(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreSpotlight.CSSearchQueryErrorCode)
        self.assertIsEnumType(CoreSpotlight.CSSearchQuerySourceOptions)

    def testConstants(self):
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeUnknown, -2000)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeIndexUnreachable, -2001)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeInvalidQuery, -2002)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeCancelled, -2003)

        self.assertIsInstance(CoreSpotlight.CSSearchQueryErrorDomain, str)

        self.assertEqual(CoreSpotlight.CSSearchQuerySourceOptionDefault, 0)
        self.assertEqual(CoreSpotlight.CSSearchQuerySourceOptionAllowMail, 1 << 0)

    def testMethods(self):
        self.assertResultIsBOOL(CoreSpotlight.CSSearchQuery.isCancelled)
        self.assertResultIsBlock(CoreSpotlight.CSSearchQuery.foundItemsHandler, b"v@")
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchQuery.setFoundItemsHandler_, 0, b"v@"
        )
        self.assertResultIsBlock(CoreSpotlight.CSSearchQuery.completionHandler, b"v@")
        self.assertArgIsBlock(
            CoreSpotlight.CSSearchQuery.setCompletionHandler_, 0, b"v@"
        )
