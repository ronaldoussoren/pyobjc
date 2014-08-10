import sys

try:
    unicode
except NameError:
    unicode = str

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKPolygon (TestCase):
        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKPolygon, objc.objc_class)

            self.assertArgCountInArg(MapKit.MKPolygon.polygonWithPoints_count_, 0, 1)
            self.assertArgIsIn(MapKit.MKPolygon.polygonWithPoints_count_, 0)

            self.assertArgCountInArg(MapKit.MKPolygon.polygonWithPoints_count_interiorPolygons_, 0, 1)
            self.assertArgIsIn(MapKit.MKPolygon.polygonWithPoints_count_interiorPolygons_, 0)

            self.assertArgCountInArg(MapKit.MKPolygon.polygonWithCoordinates_count_, 0, 1)
            self.assertArgIsIn(MapKit.MKPolygon.polygonWithCoordinates_count_, 0)

            self.assertArgCountInArg(MapKit.MKPolygon.polygonWithCoordinates_count_interiorPolygons_, 0, 1)
            self.assertArgIsIn(MapKit.MKPolygon.polygonWithCoordinates_count_interiorPolygons_, 0)

if __name__ == "__main__":
    main()
