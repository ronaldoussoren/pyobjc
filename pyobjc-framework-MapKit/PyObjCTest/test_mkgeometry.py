from PyObjCTools.TestSupport import TestCase, min_os_level
import objc

import MapKit


class TestMKGeometry(TestCase):
    @min_os_level("10.9")
    def testStructs(self):
        s = MapKit.MKCoordinateSpan()
        self.assertIsInstance(s.latitudeDelta, float)
        self.assertIsInstance(s.longitudeDelta, float)
        self.assertPickleRoundTrips(s)

        s = MapKit.MKCoordinateRegion()
        self.assertIsInstance(s.center, MapKit.CLLocationCoordinate2D)
        self.assertIsInstance(s.span, MapKit.MKCoordinateSpan)
        self.assertPickleRoundTrips(s)

        s = MapKit.MKMapPoint()
        self.assertIsInstance(s.x, float)
        self.assertIsInstance(s.y, float)
        self.assertPickleRoundTrips(s)

        s = MapKit.MKMapSize()
        self.assertIsInstance(s.width, float)
        self.assertIsInstance(s.height, float)
        self.assertPickleRoundTrips(s)

        s = MapKit.MKMapRect()
        self.assertIsInstance(s.origin, MapKit.MKMapPoint)
        self.assertIsInstance(s.size, MapKit.MKMapSize)
        self.assertPickleRoundTrips(s)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertIsInstance(MapKit.MKMapSizeWorld, MapKit.MKMapSize)
        self.assertIsInstance(MapKit.MKMapRectWorld, MapKit.MKMapRect)
        self.assertIsInstance(MapKit.MKMapRectNull, MapKit.MKMapRect)

    @min_os_level("10.9")
    def test_functions(self):
        c = MapKit.MKCoordinateSpanMake(0.5, 2.5)
        self.assertIsInstance(c, MapKit.MKCoordinateSpan)
        self.assertEqual(c, MapKit.MKCoordinateSpan(0.5, 2.5))
        self.assertEqual(c.latitudeDelta, 0.5)
        self.assertEqual(c.longitudeDelta, 2.5)

        c = MapKit.MKCoordinateRegionMake(
            MapKit.CLLocationCoordinate2D(), MapKit.MKCoordinateSpan()
        )
        self.assertIsInstance(c, MapKit.MKCoordinateRegion)
        self.assertIsInstance(c.center, MapKit.CLLocationCoordinate2D)
        self.assertIsInstance(c.span, MapKit.MKCoordinateSpan)

        c = MapKit.MKCoordinateRegionMakeWithDistance(
            MapKit.CLLocationCoordinate2D(), 1000, 1500
        )
        self.assertIsInstance(c, MapKit.MKCoordinateRegion)
        self.assertIsInstance(c.center, MapKit.CLLocationCoordinate2D)
        self.assertIsInstance(c.span, MapKit.MKCoordinateSpan)

        c = MapKit.MKMapPointForCoordinate(MapKit.CLLocationCoordinate2D())
        self.assertIsInstance(c, MapKit.MKMapPoint)

        c = MapKit.MKCoordinateForMapPoint(MapKit.MKMapPoint())
        self.assertIsInstance(c, MapKit.CLLocationCoordinate2D)

        self.assertArgHasType(MapKit.MKMetersPerMapPointAtLatitude, 0, objc._C_DBL)
        self.assertResultHasType(MapKit.MKMetersPerMapPointAtLatitude, objc._C_DBL)

        self.assertArgHasType(MapKit.MKMapPointsPerMeterAtLatitude, 0, objc._C_DBL)
        self.assertResultHasType(MapKit.MKMapPointsPerMeterAtLatitude, objc._C_DBL)

        self.assertArgHasType(
            MapKit.MKMetersBetweenMapPoints, 0, MapKit.MKMapPoint.__typestr__
        )
        self.assertArgHasType(
            MapKit.MKMetersBetweenMapPoints, 1, MapKit.MKMapPoint.__typestr__
        )
        self.assertResultHasType(MapKit.MKMetersBetweenMapPoints, objc._C_DBL)

        c = MapKit.MKMapPointMake(1.5, 2.5)
        self.assertIsInstance(c, MapKit.MKMapPoint)
        self.assertEqual(c.x, 1.5)
        self.assertEqual(c.y, 2.5)

        c = MapKit.MKMapSizeMake(1.5, 2.5)
        self.assertIsInstance(c, MapKit.MKMapSize)
        self.assertEqual(c.width, 1.5)
        self.assertEqual(c.height, 2.5)

        c = MapKit.MKMapRectMake(1.5, 2.5, 3.5, 4.5)
        self.assertIsInstance(c, MapKit.MKMapRect)
        self.assertEqual(c.origin, MapKit.MKMapPoint(1.5, 2.5))
        self.assertEqual(c.size, MapKit.MKMapSize(3.5, 4.5))

        self.assertIsInstance(MapKit.MKMapRectGetMinX(c), float)
        self.assertIsInstance(MapKit.MKMapRectGetMinY(c), float)
        self.assertIsInstance(MapKit.MKMapRectGetMidX(c), float)
        self.assertIsInstance(MapKit.MKMapRectGetMidY(c), float)
        self.assertIsInstance(MapKit.MKMapRectGetMaxX(c), float)
        self.assertIsInstance(MapKit.MKMapRectGetMaxY(c), float)
        self.assertIsInstance(MapKit.MKMapRectGetWidth(c), float)
        self.assertIsInstance(MapKit.MKMapRectGetHeight(c), float)

        self.assertIsInstance(
            MapKit.MKMapPointEqualToPoint(MapKit.MKMapPoint(), MapKit.MKMapPoint()),
            bool,
        )
        self.assertIsInstance(
            MapKit.MKMapSizeEqualToSize(MapKit.MKMapSize(), MapKit.MKMapSize()), bool
        )
        self.assertIsInstance(
            MapKit.MKMapRectEqualToRect(MapKit.MKMapRect(), MapKit.MKMapRect()), bool
        )
        self.assertIsInstance(MapKit.MKMapRectIsNull(MapKit.MKMapRect()), bool)
        self.assertIsInstance(MapKit.MKMapRectIsEmpty(MapKit.MKMapRect()), bool)
        self.assertIsInstance(MapKit.MKStringFromMapPoint(MapKit.MKMapPoint()), str)
        self.assertIsInstance(MapKit.MKStringFromMapSize(MapKit.MKMapSize()), str)
        self.assertIsInstance(MapKit.MKStringFromMapRect(MapKit.MKMapRect()), str)
        self.assertIsInstance(
            MapKit.MKMapRectUnion(MapKit.MKMapRect(), MapKit.MKMapRect()),
            MapKit.MKMapRect,
        )
        self.assertIsInstance(
            MapKit.MKMapRectIntersection(MapKit.MKMapRect(), MapKit.MKMapRect()),
            MapKit.MKMapRect,
        )
        self.assertIsInstance(
            MapKit.MKMapRectInset(MapKit.MKMapRect(), 0.0, 0.0), MapKit.MKMapRect
        )
        self.assertIsInstance(
            MapKit.MKMapRectOffset(MapKit.MKMapRect(), 0.0, 0.0), MapKit.MKMapRect
        )

        self.assertArgIsOut(MapKit.MKMapRectDivide, 1)
        self.assertArgIsOut(MapKit.MKMapRectDivide, 2)
        self.assertResultIsBOOL(MapKit.MKMapRectContainsPoint)
        self.assertResultIsBOOL(MapKit.MKMapRectContainsRect)
        self.assertResultIsBOOL(MapKit.MKMapRectIntersectsRect)

        MapKit.MKCoordinateRegionForMapRect  # XXX: Nothing to test beyond existance
        MapKit.MKMapRectRemainder  # XXX: Nothing to test beyond existance

        self.assertResultIsBOOL(MapKit.MKMapRectSpans180thMeridian)
