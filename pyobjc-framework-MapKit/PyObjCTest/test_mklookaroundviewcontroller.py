from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import MapKit


class TestMKLookAroundViewController(TestCase):
    def test_constants(self):
        self.assertIsEnumType(MapKit.MKLookAroundBadgePosition)

        self.assertEqual(MapKit.MKLookAroundBadgePositionTopLeading, 0)
        self.assertEqual(MapKit.MKLookAroundBadgePositionTopTrailing, 1)
        self.assertEqual(MapKit.MKLookAroundBadgePositionBottomTrailing, 2)

    @min_sdk_level("13.0")
    def test_protocols13_0(self):
        self.assertProtocolExists("MKLookAroundViewControllerDelegate")

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(MapKit.MKLookAroundViewController.isNavigationEnabled)
        self.assertArgIsBOOL(MapKit.MKLookAroundViewController.setNavigationEnabled_, 0)

        self.assertResultIsBOOL(MapKit.MKLookAroundViewController.showsRoadLabels)
        self.assertArgIsBOOL(MapKit.MKLookAroundViewController.setShowsRoadLabels_, 0)
