from PyObjCTools.TestSupport import TestCase

import MapKit
import CoreLocation


class TestMKGeodesicPolyline(TestCase):
    def test_methods(self):
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
