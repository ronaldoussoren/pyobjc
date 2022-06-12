from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreSpotlight


class TestCSUserQuery(TestCase):
    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertResultIsBlock(
            CoreSpotlight.CSUserQuery.foundSuggestionsHandler, b"v@"
        )
        self.assertArgIsBlock(
            CoreSpotlight.CSUserQuery.setFoundSuggestionsHandler_, 0, b"v@"
        )
