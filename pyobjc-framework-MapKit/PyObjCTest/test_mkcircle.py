from PyObjCTools.TestSupport import TestCase
import objc

import MapKit


class TestMKCircle(TestCase):
    def test_classes(self):
        self.assertIsInstance(MapKit.MKCircle, objc.objc_class)

    def test_methods(self):
        self.assertResultHasType(
            MapKit.MKCircle.boundingMapRect, MapKit.MKMapRect.__typestr__
        )
        self.assertArgHasType(
            MapKit.MKCircle.circleWithMapRect_, 0, MapKit.MKMapRect.__typestr__
        )
