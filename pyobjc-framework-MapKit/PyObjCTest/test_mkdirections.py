from PyObjCTools.TestSupport import TestCase
import objc

import MapKit

MKDirectionsHandler = b"v@@"
MKETAHandler = b"v@@"


class TestMKDirections(TestCase):
    def test_classes(self):
        self.assertIsInstance(MapKit.MKDirections, objc.objc_class)

        self.assertArgIsBlock(
            MapKit.MKDirections.calculateDirectionsWithCompletionHandler_,
            0,
            MKDirectionsHandler,
        )
        self.assertArgIsBlock(
            MapKit.MKDirections.calculateETAWithCompletionHandler_, 0, MKETAHandler
        )

        self.assertResultIsBOOL(MapKit.MKDirections.isCalculating)
