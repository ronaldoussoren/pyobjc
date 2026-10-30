from PyObjCTools.TestSupport import TestCase

import MapKit


class TestMKPolygon(TestCase):
    def test_methods(self):
        self.assertArgSizeInArg(MapKit.MKPolygon.polygonWithPoints_count_, 0, 1)
        self.assertArgIsIn(MapKit.MKPolygon.polygonWithPoints_count_, 0)

        self.assertArgSizeInArg(
            MapKit.MKPolygon.polygonWithPoints_count_interiorPolygons_, 0, 1
        )
        self.assertArgIsIn(
            MapKit.MKPolygon.polygonWithPoints_count_interiorPolygons_, 0
        )

        self.assertArgSizeInArg(MapKit.MKPolygon.polygonWithCoordinates_count_, 0, 1)
        self.assertArgIsIn(MapKit.MKPolygon.polygonWithCoordinates_count_, 0)

        self.assertArgSizeInArg(
            MapKit.MKPolygon.polygonWithCoordinates_count_interiorPolygons_, 0, 1
        )
        self.assertArgIsIn(
            MapKit.MKPolygon.polygonWithCoordinates_count_interiorPolygons_, 0
        )
