from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKReverseGeocodingRequest(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKReverseGeocodingRequest.isCancelled)
        self.assertResultIsBOOL(MapKit.MKReverseGeocodingRequest.isLoading)
        self.assertArgIsBlock(
            MapKit.MKReverseGeocodingRequest.getMapItemsWithCompletionHandler_,
            0,
            b"v@@",
        )
