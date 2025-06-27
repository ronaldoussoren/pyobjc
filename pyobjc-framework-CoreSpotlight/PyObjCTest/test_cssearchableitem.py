from PyObjCTools.TestSupport import TestCase, min_os_level


import CoreSpotlight


class TestCSSearchableItem(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreSpotlight.CSSearchableItemActionType, str)
        self.assertIsInstance(CoreSpotlight.CSSearchableItemActivityIdentifier, str)
        self.assertIsInstance(CoreSpotlight.CSQueryContinuationActionType, str)
        self.assertIsInstance(CoreSpotlight.CSSearchQueryString, str)

        self.assertIsEnumType(CoreSpotlight.CSSearchableItemUpdateListenerOptions)
        self.assertEqual(CoreSpotlight.CSSearchableItemUpdateListenerOptionDefault, 0)
        self.assertEqual(
            CoreSpotlight.CSSearchableItemUpdateListenerOptionSummarization, 1 << 1
        )
        self.assertEqual(
            CoreSpotlight.CSSearchableItemUpdateListenerOptionPriority, 1 << 2
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(CoreSpotlight.CSSearchableItem.isUpdate)
        self.assertArgIsBOOL(CoreSpotlight.CSSearchableItem.setIsUpdate_, 0)
