from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKCircle(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MapKit.MKErrorCode)
        self.assertIsEnumType(MapKit.MKFeatureVisibility)
        self.assertIsEnumType(MapKit.MKMapType)

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

        self.assertEqual(MapKit.MKMapTypeSatelliteFlyover, 3)
        self.assertEqual(MapKit.MKMapTypeHybridFlyover, 4)
        self.assertEqual(MapKit.MKMapTypeMutedStandard, 5)

        self.assertIsEnumType(MapKit.MKLocalSearchRegionPriority)
        self.assertEqual(MapKit.MKLocalSearchRegionPriorityDefault, 0)
        self.assertEqual(MapKit.MKLocalSearchRegionPriorityRequired, 1)
