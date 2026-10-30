from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKLocalSearchResponse(TestCase):
    def test_methods(self):
        self.assertResultHasType(
            MapKit.MKLocalSearchResponse.boundingRegion,
            MapKit.MKCoordinateRegion.__typestr__,
        )
