from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreSpotlight


class TestCSUserQuery(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreSpotlight.CSUserInteraction)
        self.assertEqual(CoreSpotlight.CSUserInteractionSelect, 0)
        self.assertEqual(
            CoreSpotlight.CSUserInteractionDefault,
            CoreSpotlight.CSUserInteractionSelect,
        )
        self.assertEqual(CoreSpotlight.CSUserInteractionFocus, 1)

    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertResultIsBOOL(CoreSpotlight.CSUserQueryContext.enableRankedResults)
        self.assertArgIsBOOL(
            CoreSpotlight.CSUserQueryContext.setEnableRankedResults_, 0
        )

        self.assertResultIsBlock(
            CoreSpotlight.CSUserQuery.foundSuggestionsHandler, b"v@"
        )
        self.assertArgIsBlock(
            CoreSpotlight.CSUserQuery.setFoundSuggestionsHandler_, 0, b"v@"
        )

    @min_os_level("15.0")
    def testMethods15_0(self):
        self.assertResultIsBOOL(CoreSpotlight.CSUserQueryContext.disableSemanticSearch)
        self.assertArgIsBOOL(
            CoreSpotlight.CSUserQueryContext.setDisableSemanticSearch_, 0
        )
