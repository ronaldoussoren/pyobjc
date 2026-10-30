from PyObjCTools.TestSupport import TestCase

import MapKit

MKLocalSearchCompletionHandler = b"v@@"


class TestMKLocalSearch(TestCase):
    def test_methods(self):
        self.assertArgIsBlock(
            MapKit.MKLocalSearch.startWithCompletionHandler_,
            0,
            MKLocalSearchCompletionHandler,
        )
        self.assertResultIsBOOL(MapKit.MKLocalSearch.isSearching)
