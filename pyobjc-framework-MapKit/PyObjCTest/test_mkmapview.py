import sys

try:
    unicode
except NameError:
    unicode = str

from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import MapKit

    class TestMKMapViewHelper (MapKit.NSObject):
        def mapView_regionWillChangeAnimated_(self, v, a): pass
        def mapView_regionDidChangeAnimated_(self, v, a): pass
        def mapViewDidFinishRenderingMap_fullyRendered_(self, v, a): pass
        def mapView_annotationView_didChangeDragState_fromOldState_(self, v, av, s1, s2): pass

    class TestMKMapView (TestCase):
        @min_os_level("10.9")
        def testConstants(self):
            self.assertEqual(MapKit.MKUserTrackingModeNone, 0)
            self.assertEqual(MapKit.MKUserTrackingModeFollow, 1)
            self.assertEqual(MapKit.MKUserTrackingModeFollowWithHeading, 2)

            self.assertEqual(MapKit.MKOverlayLevelAboveRoads, 0)
            self.assertEqual(MapKit.MKOverlayLevelAboveLabels, 1)

        @min_os_level("10.9")
        def testProtocols(self):
            self.assertIsInstance(objc.protocolNamed("MKMapViewDelegate"), objc.formal_protocol)

            self.assertArgIsBOOL(TestMKMapViewHelper.mapView_regionWillChangeAnimated_, 1)
            self.assertArgIsBOOL(TestMKMapViewHelper.mapView_regionDidChangeAnimated_, 1)
            self.assertArgIsBOOL(TestMKMapViewHelper.mapViewDidFinishRenderingMap_fullyRendered_, 1)
            self.assertArgHasType(TestMKMapViewHelper.mapView_annotationView_didChangeDragState_fromOldState_, 2, objc._C_UInteger)
            self.assertArgHasType(TestMKMapViewHelper.mapView_annotationView_didChangeDragState_fromOldState_, 3, objc._C_UInteger)

        @min_os_level("10.9")
        def testClasses(self):
            self.assertIsInstance(MapKit.MKMapView, objc.objc_class)

            self.assertArgIsBOOL(MapKit.MKMapView.setRegion_animated_, 1)
            self.assertArgIsBOOL(MapKit.MKMapView.setCenterCoordinate_animated_, 1)
            self.assertArgIsBOOL(MapKit.MKMapView.setVisibleMapRect_animated_, 1)
            self.assertArgIsBOOL(MapKit.MKMapView.setVisibleMapRect_edgePadding_animated_, 2)
            self.assertArgIsBOOL(MapKit.MKMapView.setCamera_animated_, 1)

            self.assertArgIsBOOL(MapKit.MKMapView.setZoomEnabled_, 0)
            self.assertArgIsBOOL(MapKit.MKMapView.setScrollEnabled_, 0)
            self.assertArgIsBOOL(MapKit.MKMapView.setRotateEnabled_, 0)
            self.assertArgIsBOOL(MapKit.MKMapView.setPitchEnabled_, 0)

            self.assertResultIsBOOL(MapKit.MKMapView.isZoomEnabled)
            self.assertResultIsBOOL(MapKit.MKMapView.isScrollEnabled)
            self.assertResultIsBOOL(MapKit.MKMapView.isRotateEnabled)
            self.assertResultIsBOOL(MapKit.MKMapView.isPitchEnabled)

            self.assertArgIsBOOL(MapKit.MKMapView.setShowsCompas_, 0)
            self.assertArgIsBOOL(MapKit.MKMapView.setShowsZoomControls_, 0)
            self.assertArgIsBOOL(MapKit.MKMapView.setShowsScale_, 0)
            self.assertArgIsBOOL(MapKit.MKMapView.setShowsPointsOfInterest_, 0)
            self.assertArgIsBOOL(MapKit.MKMapView.setShowsBuildings_, 0)
            self.assertArgIsBOOL(MapKit.MKMapView.setShowsUserLocation_, 0)

            self.assertResultIsBOOL(MapKit.MKMapView.showsCompas)
            self.assertResultIsBOOL(MapKit.MKMapView.showsZoomControls)
            self.assertResultIsBOOL(MapKit.MKMapView.showsScale)
            self.assertResultIsBOOL(MapKit.MKMapView.showsPointsOfInterest)
            self.assertResultIsBOOL(MapKit.MKMapView.showsBuildings)
            self.assertResultIsBOOL(MapKit.MKMapView.showsUserLocation)

            self.assertResultIsBOOL(MapKit.MKMapView.isUserLocationVisible)
            self.assertArgIsBOOL(MapKit.MKMapView.selectAnnotation_animated_, 1)
            self.assertArgIsBOOL(MapKit.MKMapView.deselectAnnotation_animated_, 1)
            self.assertArgIsBOOL(MapKit.MKMapView.showAnnotations_animated_, 1)



if __name__ == "__main__":
    main()
