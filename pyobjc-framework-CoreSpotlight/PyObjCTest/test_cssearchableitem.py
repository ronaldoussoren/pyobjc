from PyObjCTools.TestSupport import TestCase, min_os_level


import CoreSpotlight


class TestCSSearchableItem(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreSpotlight.CSSearchableItemActionType, str)
        self.assertIsInstance(CoreSpotlight.CSSearchableItemActivityIdentifier, str)
        self.assertIsInstance(CoreSpotlight.CSQueryContinuationActionType, str)
        self.assertIsInstance(CoreSpotlight.CSSearchQueryString, str)

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(CoreSpotlight.CSSearchableItem.isUpdate)
        self.assertArgIsBOOL(CoreSpotlight.CSSearchableItem.setIsUpdate_, 0)
