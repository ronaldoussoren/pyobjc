from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKSelectionAccessory(TestCase):
    def test_enum(self):
        self.assertIsEnumType(MapKit.MKMapItemDetailSelectionAccessoryCalloutStyle)
        self.assertEqual(
            MapKit.MKMapItemDetailSelectionAccessoryCalloutStyleAutomatic, 0
        )
        self.assertEqual(MapKit.MKMapItemDetailSelectionAccessoryCalloutStyleFull, 1)
        self.assertEqual(MapKit.MKMapItemDetailSelectionAccessoryCalloutStyleCompact, 2)
