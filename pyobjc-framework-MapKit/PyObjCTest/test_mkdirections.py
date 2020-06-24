from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit

MKDirectionsHandler = b"v@@"
MKETAHandler = b"v@@"


class TestMKDirections(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
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
