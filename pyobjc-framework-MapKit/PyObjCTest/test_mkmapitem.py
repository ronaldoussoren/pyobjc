from PyObjCTools.TestSupport import TestCase, min_os_level

import MapKit


class TestMKMapItem(TestCase):
    def test_constants(self):
        self.assertIsInstance(MapKit.MKLaunchOptionsDirectionsModeKey, str)
        self.assertIsInstance(MapKit.MKLaunchOptionsMapTypeKey, str)
        self.assertIsInstance(MapKit.MKLaunchOptionsShowsTrafficKey, str)
        self.assertIsInstance(MapKit.MKLaunchOptionsDirectionsModeDriving, str)
        self.assertIsInstance(MapKit.MKLaunchOptionsDirectionsModeWalking, str)
        self.assertIsInstance(MapKit.MKLaunchOptionsMapCenterKey, str)
        self.assertIsInstance(MapKit.MKLaunchOptionsMapSpanKey, str)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(MapKit.MKLaunchOptionsCameraKey, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(MapKit.MKLaunchOptionsDirectionsModeTransit, str)
        self.assertIsInstance(MapKit.MKLaunchOptionsDirectionsModeCycling, str)

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(MapKit.MKLaunchOptionsDirectionsModeDefault, str)

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(MapKit.MKMapItemTypeIdentifier, str)
        self.assertIsInstance(MapKit.MKMapViewDefaultAnnotationViewReuseIdentifier, str)
        self.assertIsInstance(
            MapKit.MKMapViewDefaultClusterAnnotationViewReuseIdentifier, str
        )

    @min_os_level("14.4")
    def test_methods14_4(self):
        self.assertArgIsBlock(
            MapKit.MKMapItem.openInMapsWithLaunchOptions_completionHandler_, 1, b"vZ"
        )
        self.assertArgIsBlock(
            MapKit.MKMapItem.openMapsWithItems_launchOptions_completionHandler_,
            2,
            b"vZ",
        )

    def test_classes(self):
        self.assertResultIsBOOL(MapKit.MKMapItem.isCurrentLocation)
        self.assertResultIsBOOL(MapKit.MKMapItem.openInMapsWithLaunchOptions_)
        self.assertResultIsBOOL(MapKit.MKMapItem.openMapsWithItems_launchOptions_)
