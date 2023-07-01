from PyObjCTools.TestSupport import TestCase

import CoreSpotlight


class TestCoreSpotlight(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreSpotlight.CoreSpotlightVersionNumber, float)
        self.assertIsInstance(CoreSpotlight.CoreSpotlightVersionString, bytes)

        self.assertNotHasAtrr(CoreSpotlight, "CoreSpotlightAPIVersion")


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(CoreSpotlight)
