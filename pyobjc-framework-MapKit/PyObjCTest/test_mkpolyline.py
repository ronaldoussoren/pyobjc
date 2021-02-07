from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKPolyline(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKPolyline, objc.objc_class)

        self.assertArgSizeInArg(MapKit.MKPolyline.polylineWithPoints_count_, 0, 1)
        self.assertArgIsIn(MapKit.MKPolyline.polylineWithPoints_count_, 0)

        self.assertArgSizeInArg(MapKit.MKPolyline.polylineWithCoordinates_count_, 0, 1)
        self.assertArgIsIn(MapKit.MKPolyline.polylineWithCoordinates_count_, 0)
