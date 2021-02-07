from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKMapCameraZoomRange(TestCase):
    @min_os_level("10.15")
    def test_constants(self):
        self.assertIsInstance(MapKit.MKMapCameraZoomDefault, float)
