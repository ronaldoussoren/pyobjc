from PyObjCTools.TestSupport import TestCase


import CoreSpotlight


class TestCSSearchQuery(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreSpotlight.CSSearchQueryErrorCode)

    def testConstants(self):
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeUnknown, -2000)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeIndexUnreachable, -2001)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeInvalidQuery, -2002)
        self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeCancelled, -2003)

        self.assertIsInstance(CoreSpotlight.CSSearchQueryErrorDomain, str)

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
