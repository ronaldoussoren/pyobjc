from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKMapConfiguration(TestCase):
    def test_constants(self):
        self.assertIsEnumType(MapKit.MKMapLandscape)
        self.assertEqual(MapKit.MKMapLandscapeDefault, 0)
        self.assertEqual(MapKit.MKMapLandscapeDetailed, 1)

        self.assertIsEnumType(MapKit.MKMapElevationStyle)
        self.assertEqual(MapKit.MKMapElevationStyleFlat, 0)
        self.assertEqual(MapKit.MKMapElevationStyleRealistic, 1)
