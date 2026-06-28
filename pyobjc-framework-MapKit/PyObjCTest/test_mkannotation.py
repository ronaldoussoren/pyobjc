from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKAnnotationHelper(MapKit.NSObject):
    def coordinate(self):
        return 1

    def setCoordinate_(self, value):
        pass


class TestMKAnnotation(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MKAnnotation", MapKit)

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMKAnnotationHelper.coordinate, MapKit.CLLocationCoordinate2D.__typestr__
        )
        self.assertArgHasType(
            TestMKAnnotationHelper.setCoordinate_,
            0,
            MapKit.CLLocationCoordinate2D.__typestr__,
        )
