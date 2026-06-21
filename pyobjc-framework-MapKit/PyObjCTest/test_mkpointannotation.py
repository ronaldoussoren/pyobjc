from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKPointAnnotation(TestCase):
    @min_os_level("10.9")
    def test_classes(self):
        self.assertIsInstance(MapKit.MKPointAnnotation, objc.objc_class)
