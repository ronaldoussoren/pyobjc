from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKPolygonRenderer(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKPolygonRenderer, objc.objc_class)
