from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKMultiPoint(TestCase):
    def test_methods(self):
        self.assertResultIsVariableSize(
            MapKit.MKMultiPoint.points
        )  # XXX: Gone in 10.11 SDK headers?

        self.assertArgSizeInArg(MapKit.MKMultiPoint.getCoordinates_range_, 0, 1)
        self.assertArgIsOut(MapKit.MKMultiPoint.getCoordinates_range_, 0)
