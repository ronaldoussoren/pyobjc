from PyObjCTools.TestSupport import TestCase

import AppTrackingTransparency


class TestAppTrackingTransparency(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            AppTrackingTransparency.AppTrackingTransparencyVersionNumber, float
        )
        self.assertIsInstance(
            AppTrackingTransparency.AppTrackingTransparencyVersionString, bytes
        )
