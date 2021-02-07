from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKShape(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKShape, objc.objc_class)
