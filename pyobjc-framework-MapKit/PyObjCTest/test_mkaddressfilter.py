from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKAddressFilter(TestCase):
    def test_enum(self):
        self.assertIsEnumType(MapKit.MKAddressFilterOption)
        self.assertEqual(MapKit.MKAddressFilterOptionCountry, 1 << 0)
        self.assertEqual(MapKit.MKAddressFilterOptionAdministrativeArea, 1 << 1)
        self.assertEqual(MapKit.MKAddressFilterOptionSubAdministrativeArea, 1 << 2)
        self.assertEqual(MapKit.MKAddressFilterOptionLocality, 1 << 3)
        self.assertEqual(MapKit.MKAddressFilterOptionSubLocality, 1 << 4)
        self.assertEqual(MapKit.MKAddressFilterOptionPostalCode, 1 << 5)

    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKAddressFilter.includesOptions_)
        self.assertResultIsBOOL(MapKit.MKAddressFilter.excludesOptions_)
