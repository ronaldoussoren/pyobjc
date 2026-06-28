from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKTileOverlay(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MapKit.MKTileOverlay.isGeometryFlipped)
        self.assertArgIsBOOL(MapKit.MKTileOverlay.setGeometryFlipped_, 0)

        self.assertResultIsBOOL(MapKit.MKTileOverlay.canReplaceMapContent)
        self.assertArgIsBOOL(MapKit.MKTileOverlay.setCanReplaceMapContent_, 0)

        self.assertArgIsBlock(MapKit.MKTileOverlay.loadTileAtPath_result_, 1, b"v@@")

    def test_structs(self):
        c = MapKit.MKTileOverlayPath()
        self.assertIsInstance(c.x, int)
        self.assertIsInstance(c.y, int)
        self.assertIsInstance(c.z, int)
        self.assertIsInstance(c.contentScaleFactor, float)
        self.assertPickleRoundTrips(c)
