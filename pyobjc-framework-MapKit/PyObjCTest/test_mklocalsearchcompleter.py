from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import MapKit


class TestMKLocalSearchCompleter(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MapKit.MKLocalSearchCompleterResultType)
        self.assertEqual(MapKit.MKLocalSearchCompleterResultTypeAddress, 1 << 0)
        self.assertEqual(MapKit.MKLocalSearchCompleterResultTypePointOfInterest, 1 << 1)
        self.assertEqual(MapKit.MKLocalSearchCompleterResultTypeQuery, 1 << 2)
        self.assertEqual(MapKit.MKLocalSearchCompleterResultTypePhysicalFeature, 1 << 3)

        self.assertIsEnumType(MapKit.MKSearchCompletionFilterType)
        self.assertEqual(MapKit.MKSearchCompletionFilterTypeLocationsAndQueries, 0)
        self.assertEqual(MapKit.MKSearchCompletionFilterTypeLocationsOnly, 1)

    @min_os_level("10.11")
    def test_methods(self):
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
    def test_protocols(self):
        self.assertProtocolExists("MKLocalSearchCompleterDelegate", MapKit)
