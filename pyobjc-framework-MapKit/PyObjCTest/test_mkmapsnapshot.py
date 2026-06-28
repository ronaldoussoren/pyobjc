from PyObjCTools.TestSupport import TestCase

import MapKit
import CoreLocation


class TestMKMapSnapshot(TestCase):
    def test_methods(self):
        self.assertArgHasType(
            MapKit.MKMapSnapshot.pointForCoordinate_,
            0,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )
