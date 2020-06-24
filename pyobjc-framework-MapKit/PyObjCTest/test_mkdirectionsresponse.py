from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKDirectionsRequest(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKDirectionsResponse, objc.objc_class)
        self.assertIsInstance(MapKit.MKRoute, objc.objc_class)
        self.assertIsInstance(MapKit.MKRouteStep, objc.objc_class)
        self.assertIsInstance(MapKit.MKETAResponse, objc.objc_class)
