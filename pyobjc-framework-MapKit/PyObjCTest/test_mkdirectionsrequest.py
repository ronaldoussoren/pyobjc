from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKDirectionsRequest(TestCase):
    def test_constants(self):
        self.assertIsEnumType(MapKit.MKDirectionsRoutePreference)
        self.assertEqual(MapKit.MKDirectionsRoutePreferenceAny, 0)
        self.assertEqual(MapKit.MKDirectionsRoutePreferenceAvoid, 1)

    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKDirectionsRequest, objc.objc_class)

        self.assertResultIsBOOL(MapKit.MKDirectionsRequest.requestsAlternateRoutes)
        self.assertArgIsBOOL(MapKit.MKDirectionsRequest.setRequestsAlternateRoutes_, 0)

        self.assertResultIsBOOL(MapKit.MKDirectionsRequest.isDirectionsRequestURL_)
