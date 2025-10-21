from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit
import CoreLocation


class TestMKMapSnapshot(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKMapSnapshot, objc.objc_class)

    def test_methods(self):
        self.assertArgHasType(
            MapKit.MKMapSnapshot.pointForCoordinate_,
            0,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )
