from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import MapKit


class TestMKLocalSearchCompleter(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MapKit.MKLocalSearchCompleterResultType)
        self.assertIsEnumType(MapKit.MKSearchCompletionFilterType)

    def testConstants(self):
        self.assertEqual(MapKit.MKSearchCompletionFilterTypeLocationsAndQueries, 0)
        self.assertEqual(MapKit.MKSearchCompletionFilterTypeLocationsOnly, 1)

        self.assertEqual(MapKit.MKLocalSearchCompleterResultTypeAddress, 1 << 0)
        self.assertEqual(MapKit.MKLocalSearchCompleterResultTypePointOfInterest, 1 << 1)
        self.assertEqual(MapKit.MKLocalSearchCompleterResultTypeQuery, 1 << 2)
        self.assertEqual(MapKit.MKLocalSearchCompleterResultTypePhysicalFeature, 1 << 3)

    @min_os_level("10.11")
    def testMethods(self):
        self.assertResultIsBOOL(MapKit.MKLocalSearchCompleter.isSearching)

        self.assertResultHasType(
            MapKit.MKLocalSearchCompleter.region, MapKit.MKCoordinateRegion.__typestr__
        )
        self.assertArgHasType(
            MapKit.MKLocalSearchCompleter.setRegion_,
            0,
            MapKit.MKCoordinateRegion.__typestr__,
        )

    @min_sdk_level("10.12")
    def testProtocols(self):
        self.assertProtocolExists("MKLocalSearchCompleterDelegate")
