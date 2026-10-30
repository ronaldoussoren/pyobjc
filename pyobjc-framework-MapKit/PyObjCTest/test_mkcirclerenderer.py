from PyObjCTools.TestSupport import TestCase
import objc

import MapKit


class TestMKCircleRenderer(TestCase):
    def test_classes(self):
        self.assertIsInstance(MapKit.MKCircleRenderer, objc.objc_class)
