from PyObjCTools.TestSupport import TestCase

import CoreSpotlight


class TestCoreSpotlight(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreSpotlight.CoreSpotlightVersionNumber, float)
        self.assertIsInstance(CoreSpotlight.CoreSpotlightVersionString, bytes)
