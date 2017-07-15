from PyObjCTools.TestSupport import *

import CoreSpotlight

class TestCSSearchableItem (TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreSpotlight.CSSearchableItemActionType, unicode)
        self.assertIsInstance(CoreSpotlight.CSSearchableItemActivityIdentifier, unicode)
        self.assertIsInstance(CoreSpotlight.CSQueryContinuationActionType, unicode)
        self.assertIsInstance(CoreSpotlight.CSSearchQueryString, unicode)

if __name__ == "__main__":
    main()
