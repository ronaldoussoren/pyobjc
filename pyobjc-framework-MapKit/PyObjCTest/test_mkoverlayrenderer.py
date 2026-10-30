from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKOverlayRenderer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKOverlayRenderer.canDrawMapRect_zoomScale_)

    def test_functions(self):
        MapKit.MKRoadWidthAtZoomScale
