from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit
import CoreLocation


class TestMKMapCamera(TestCase):
    def test_methods(self):
        self.assertArgHasType(
            MapKit.MKMapCamera.cameraLookingAtCenterCoordinate_fromEyeCoordinate_eyeAltitude_,
            0,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )
        self.assertArgHasType(
            MapKit.MKMapCamera.cameraLookingAtCenterCoordinate_fromEyeCoordinate_eyeAltitude_,
            1,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )
        self.assertResultHasType(
            MapKit.MKMapCamera.centerCoordinate,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )
        self.assertArgHasType(
            MapKit.MKMapCamera.setCenterCoordinate_,
            0,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBOOL(
            MapKit.MKMapCamera.cameraLookingAtMapItem_forViewSize_allowPitch_, 2
        )
