from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKCircle(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MapKit.MKErrorCode)
        self.assertIsEnumType(MapKit.MKFeatureVisibility)
        self.assertIsEnumType(MapKit.MKMapType)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(MapKit.MKMapTypeStandard, 0)
        self.assertEqual(MapKit.MKMapTypeSatellite, 1)
        self.assertEqual(MapKit.MKMapTypeHybrid, 2)

        self.assertIsInstance(MapKit.MKErrorDomain, str)

        self.assertEqual(MapKit.MKErrorUnknown, 1)
        self.assertEqual(MapKit.MKErrorServerFailure, 2)
        self.assertEqual(MapKit.MKErrorLoadingThrottled, 3)
        self.assertEqual(MapKit.MKErrorPlacemarkNotFound, 4)
        self.assertEqual(MapKit.MKErrorDirectionsNotFound, 5)
        self.assertEqual(MapKit.MKErrorDecodingFailed, 6)

        self.assertEqual(MapKit.MKFeatureVisibilityAdaptive, 0)
        self.assertEqual(MapKit.MKFeatureVisibilityHidden, 1)
        self.assertEqual(MapKit.MKFeatureVisibilityVisible, 2)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(MapKit.MKMapTypeSatelliteFlyover, 3)
        self.assertEqual(MapKit.MKMapTypeHybridFlyover, 4)
        self.assertEqual(MapKit.MKMapTypeMutedStandard, 5)
