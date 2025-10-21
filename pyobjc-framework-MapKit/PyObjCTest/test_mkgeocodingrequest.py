from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKGeocodingRequest(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKGeocodingRequest.isCancelled)
        self.assertResultIsBOOL(MapKit.MKGeocodingRequest.isLoading)
        self.assertArgIsBlock(
            MapKit.MKGeocodingRequest.getMapItemsWithCompletionHandler_, 0, b"v@@"
        )
