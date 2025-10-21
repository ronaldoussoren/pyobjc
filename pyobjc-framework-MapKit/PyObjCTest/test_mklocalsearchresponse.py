from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKLocalSearchResponse(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKLocalSearchResponse, objc.objc_class)

    def test_methods(self):
        self.assertResultHasType(
            MapKit.MKLocalSearchResponse.boundingRegion,
            MapKit.MKCoordinateRegion.__typestr__,
        )
