from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKOverlayRenderer(TestCase):
    @min_os_level("10.9")
    def testClasses(self):
        self.assertIsInstance(MapKit.MKOverlayRenderer, objc.objc_class)

        self.assertResultIsBOOL(MapKit.MKOverlayRenderer.canDrawMapRect_zoomScale_)

    @min_os_level("10.9")
    def testFunctions(self):
        MapKit.MKRoadWidthAtZoomScale
