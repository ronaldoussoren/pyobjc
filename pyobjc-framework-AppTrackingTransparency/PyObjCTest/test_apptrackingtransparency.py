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


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(AppTrackingTransparency)
