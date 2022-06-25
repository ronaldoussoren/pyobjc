from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKMapConfiguration(TestCase):
    def test_constants(self):
        self.assertIsEnumType(MapKit.MKMapElevationStyle)
        self.assertEqual(MapKit.MKMapElevationStyleFlat, 0)
        self.assertEqual(MapKit.MKMapElevationStyleRealistic, 1)
