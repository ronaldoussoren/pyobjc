from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKPinAnnotationView(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MapKit.MKPinAnnotationColor)
        self.assertEqual(MapKit.MKPinAnnotationColorRed, 0)
        self.assertEqual(MapKit.MKPinAnnotationColorGreen, 1)
        self.assertEqual(MapKit.MKPinAnnotationColorPurple, 2)

    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKPinAnnotationView.animatesDrop)
        self.assertArgIsBOOL(MapKit.MKPinAnnotationView.setAnimatesDrop_, 0)
