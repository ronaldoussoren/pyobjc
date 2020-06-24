from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKUserLocation(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKUserLocation, objc.objc_class)

        self.assertResultIsBOOL(MapKit.MKUserLocation.isUpdating)
