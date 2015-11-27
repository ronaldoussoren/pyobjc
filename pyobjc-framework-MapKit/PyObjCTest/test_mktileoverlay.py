import sys

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKTileOverlay (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKTileOverlay, objc.objc_class)

            self.assertResultIsBOOL(MapKit.MKTileOverlay.isGeometryFlipped)
            self.assertArgIsBOOL(MapKit.MKTileOverlay.setGeometryFlipped_, 0)

            self.assertResultIsBOOL(MapKit.MKTileOverlay.canReplaceMapContent)
            self.assertArgIsBOOL(MapKit.MKTileOverlay.setCanReplaceMapContent_, 0)

            self.assertArgIsBlock(MapKit.MKTileOverlay.loadTileAtPath_result_, 1, b"v@@")

        @min_os_level("10.9")
        def testStructs(self):
            c = MapKit.MKTileOverlayPath()
            self.assertIsInstance(c.x, int)
            self.assertIsInstance(c.y, int)
            self.assertIsInstance(c.z, int)
            self.assertIsInstance(c.contentScaleFactor, float)



if __name__ == "__main__":
    main()
