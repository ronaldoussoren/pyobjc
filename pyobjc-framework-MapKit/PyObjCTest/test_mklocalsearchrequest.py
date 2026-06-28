from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKLocalSearchRequest(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MapKit.MKLocalSearchResultType)
        self.assertEqual(MapKit.MKLocalSearchResultTypeAddress, 1 << 0)
        self.assertEqual(MapKit.MKLocalSearchResultTypePointOfInterest, 1 << 1)
        self.assertEqual(MapKit.MKLocalSearchResultTypePhysicalFeature, 1 << 2)
