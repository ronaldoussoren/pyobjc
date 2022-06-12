from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKMapCamera(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKMapCamera, objc.objc_class)

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBOOL(
            MapKit.MKMapCamera.cameraLookingAtMapItem_forViewSize_allowPitch_, 2
        )
