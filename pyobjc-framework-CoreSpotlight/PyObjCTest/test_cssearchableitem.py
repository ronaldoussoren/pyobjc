from PyObjCTools.TestSupport import TestCase


import CoreSpotlight


class TestCSSearchableItem(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreSpotlight.CSSearchableItemActionType, str)
        self.assertIsInstance(CoreSpotlight.CSSearchableItemActivityIdentifier, str)
        self.assertIsInstance(CoreSpotlight.CSQueryContinuationActionType, str)
        self.assertIsInstance(CoreSpotlight.CSSearchQueryString, str)
