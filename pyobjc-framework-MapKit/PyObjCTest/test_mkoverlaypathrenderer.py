from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKOverlayPathRenderer(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKOverlayPathRenderer.shouldRasterize)
        self.assertArgIsBOOL(MapKit.MKOverlayPathRenderer.setShouldRasterize_, 0)
