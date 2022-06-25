from PyObjCTools.TestSupport import TestCase, min_os_level
import MapKit


class TestMKOverlayHelper(MapKit.NSObject):
    def intersectsMapRect_(self, r):
        return 1

    def canReplaceMapContent(self):
        return 0

    def boundingMapRect(self):
        return 0

    def coordinate(self):
        return 0


class TestMKOverlay(TestCase):
    @min_os_level("10.9")
    def testProtocols(self):
        self.assertProtocolExists("MKOverlay")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestMKOverlayHelper.intersectsMapRect_)
        self.assertArgHasType(
            TestMKOverlayHelper.intersectsMapRect_, 0, MapKit.MKMapRect.__typestr__
        )
        self.assertResultIsBOOL(TestMKOverlayHelper.canReplaceMapContent)
        self.assertResultHasType(
            TestMKOverlayHelper.coordinate, MapKit.CLLocationCoordinate2D.__typestr__
        )
        self.assertResultHasType(
            TestMKOverlayHelper.boundingMapRect, MapKit.MKMapRect.__typestr__
        )
