from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit
import CoreLocation


class TestMKGeodesicPolyline(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKGeodesicPolyline, objc.objc_class)

        self.assertArgSizeInArg(
            MapKit.MKGeodesicPolyline.polylineWithPoints_count_, 0, 1
        )
        self.assertArgHasType(
            MapKit.MKGeodesicPolyline.polylineWithPoints_count_,
            0,
            b"n^" + MapKit.MKMapPoint.__typestr__,
        )
        self.assertArgIsIn(MapKit.MKGeodesicPolyline.polylineWithPoints_count_, 0)

        self.assertArgSizeInArg(
            MapKit.MKGeodesicPolyline.polylineWithCoordinates_count_, 0, 1
        )
        self.assertArgHasType(
            MapKit.MKGeodesicPolyline.polylineWithCoordinates_count_,
            0,
            b"n^" + CoreLocation.CLLocationCoordinate2D.__typestr__,
        )
        self.assertArgIsIn(MapKit.MKGeodesicPolyline.polylineWithCoordinates_count_, 0)
