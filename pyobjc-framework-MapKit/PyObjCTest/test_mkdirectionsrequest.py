from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKDirectionsRequest(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MapKit.MKDirectionsRoutePreference)
        self.assertEqual(MapKit.MKDirectionsRoutePreferenceAny, 0)
        self.assertEqual(MapKit.MKDirectionsRoutePreferenceAvoid, 1)

    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKDirectionsRequest.requestsAlternateRoutes)
        self.assertArgIsBOOL(MapKit.MKDirectionsRequest.setRequestsAlternateRoutes_, 0)

        self.assertResultIsBOOL(MapKit.MKDirectionsRequest.isDirectionsRequestURL_)
