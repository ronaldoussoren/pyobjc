from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKPolyline(TestCase):
    def test_methods(self):
        self.assertArgSizeInArg(MapKit.MKPolyline.polylineWithPoints_count_, 0, 1)
        self.assertArgIsIn(MapKit.MKPolyline.polylineWithPoints_count_, 0)

        self.assertArgSizeInArg(MapKit.MKPolyline.polylineWithCoordinates_count_, 0, 1)
        self.assertArgIsIn(MapKit.MKPolyline.polylineWithCoordinates_count_, 0)
