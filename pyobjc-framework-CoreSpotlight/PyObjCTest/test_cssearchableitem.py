from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:

    import CoreSpotlight

    class TestCSSearchableItem (TestCase):
        def testConstants(self):
            self.assertIsInstance(CoreSpotlight.CSSearchableItemActionType, unicode)
            self.assertIsInstance(CoreSpotlight.CSSearchableItemActivityIdentifier, unicode)
            self.assertIsInstance(CoreSpotlight.CSQueryContinuationActionType, unicode)
            self.assertIsInstance(CoreSpotlight.CSSearchQueryString, unicode)

if __name__ == "__main__":
    main()
