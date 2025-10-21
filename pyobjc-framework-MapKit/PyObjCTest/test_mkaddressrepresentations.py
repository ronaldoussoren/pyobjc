from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKAddressRepresentations(TestCase):
    def test_enum(self):
        self.assertIsEnumType(MapKit.MKAddressRepresentationsContextStyle)
        self.assertEqual(MapKit.MKAddressRepresentationsContextStyleAutomatic, 0)
        self.assertEqual(MapKit.MKAddressRepresentationsContextStyleShort, 1)
        self.assertEqual(MapKit.MKAddressRepresentationsContextStyleFull, 2)

    @min_os_level("26.0")
    def test_methods(self):
        self.assertArgIsBOOL(
            MapKit.MKAddressRepresentations.fullAddressIncludingRegion_singleLine_, 0
        )
        self.assertArgIsBOOL(
            MapKit.MKAddressRepresentations.fullAddressIncludingRegion_singleLine_, 1
        )
