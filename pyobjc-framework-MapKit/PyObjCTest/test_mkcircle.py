from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKCircle(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKCircle, objc.objc_class)

    def test_methods(self):
        self.assertResultHasType(
            MapKit.MKCircle.boundingMapRect, MapKit.MKMapRect.__typestr__
        )
        self.assertArgHasType(
            MapKit.MKCircle.circleWithMapRect_, 0, MapKit.MKMapRect.__typestr__
        )
