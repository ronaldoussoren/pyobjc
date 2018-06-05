from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:

    import CoreSpotlight

    class TestCSSearchQuery (TestCase):
        def testConstants(self):
            self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeUnknown, -2000)
            self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeIndexUnreachable, -2001)
            self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeInvalidQuery, -2002)
            self.assertEqual(CoreSpotlight.CSSearchQueryErrorCodeCancelled, -2003)

            self.assertIsInstance(CoreSpotlight.CSSearchQueryErrorDomain, unicode)

        def testMethods(self):
            self.assertResultIsBOOL(CoreSpotlight.CSSearchQuery.isCancelled)
            self.assertResultIsBlock(CoreSpotlight.CSSearchQuery.foundItemsHandler, b'v@')
            self.assertArgIsBlock(CoreSpotlight.CSSearchQuery.setFoundItemsHandler_, 0, b'v@')
            self.assertResultIsBlock(CoreSpotlight.CSSearchQuery.completionHandler, b'v@')
            self.assertArgIsBlock(CoreSpotlight.CSSearchQuery.setCompletionHandler_, 0, b'v@')


if __name__ == "__main__":
    main()
