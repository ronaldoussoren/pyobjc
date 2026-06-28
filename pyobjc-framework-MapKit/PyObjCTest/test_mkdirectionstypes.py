from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKDirectionsTypes(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MapKit.MKDirectionsTransportType)

    def test_constants(self):
        self.assertEqual(MapKit.MKDirectionsTransportTypeAutomobile, 1 << 0)
        self.assertEqual(MapKit.MKDirectionsTransportTypeWalking, 1 << 1)
        self.assertEqual(MapKit.MKDirectionsTransportTypeTransit, 1 << 2)
        self.assertEqual(MapKit.MKDirectionsTransportTypeCycling, 1 << 3)
        self.assertEqual(MapKit.MKDirectionsTransportTypeAny, 0x0FFFFFFF)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertEqual(MapKit.MKDirectionsTransportTypeTransit, 1 << 2)
