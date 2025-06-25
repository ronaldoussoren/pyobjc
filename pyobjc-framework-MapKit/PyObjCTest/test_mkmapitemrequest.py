from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKMapItemReuqest(TestCase):
    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKMapItemRequest.isCancelled)
        self.assertResultIsBOOL(MapKit.MKMapItemRequest.isLoading)
