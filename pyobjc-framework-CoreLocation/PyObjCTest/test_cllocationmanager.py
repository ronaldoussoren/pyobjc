import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLLocationManager(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreLocation.CLAccuracyAuthorization)
        self.assertIsEnumType(CoreLocation.CLActivityType)
        self.assertIsEnumType(CoreLocation.CLAuthorizationStatus)
        self.assertIsEnumType(CoreLocation.CLDeviceOrientation)

    @min_os_level("10.6")
    def testMethods(self):
        self.assertResultIsBOOL(
            CoreLocation.CLLocationManager.alloc().init().locationServicesEnabled
        )

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(CoreLocation.CLDeviceOrientationUnknown, 0)
        self.assertEqual(CoreLocation.CLDeviceOrientationPortrait, 1)
        self.assertEqual(CoreLocation.CLDeviceOrientationPortraitUpsideDown, 2)
        self.assertEqual(CoreLocation.CLDeviceOrientationLandscapeLeft, 3)
        self.assertEqual(CoreLocation.CLDeviceOrientationLandscapeRight, 4)
        self.assertEqual(CoreLocation.CLDeviceOrientationFaceUp, 5)
        self.assertEqual(CoreLocation.CLDeviceOrientationFaceDown, 6)

        self.assertEqual(CoreLocation.kCLAuthorizationStatusNotDetermined, 0)
        self.assertEqual(CoreLocation.kCLAuthorizationStatusRestricted, 1)
        self.assertEqual(CoreLocation.kCLAuthorizationStatusDenied, 2)
        self.assertEqual(CoreLocation.kCLAuthorizationStatusAuthorizedAlways, 3)
        self.assertEqual(
            CoreLocation.kCLAuthorizationStatusAuthorized,
            CoreLocation.kCLAuthorizationStatusAuthorizedAlways,
        )

        self.assertEqual(CoreLocation.CLActivityTypeOther, 1)
        self.assertEqual(CoreLocation.CLActivityTypeAutomotiveNavigation, 2)
        self.assertEqual(CoreLocation.CLActivityTypeFitness, 3)
        self.assertEqual(CoreLocation.CLActivityTypeOtherNavigation, 4)
        self.assertEqual(CoreLocation.CLActivityTypeAirborne, 5)

        self.assertEqual(CoreLocation.CLAccuracyAuthorizationFullAccuracy, 0)
        self.assertEqual(CoreLocation.CLAccuracyAuthorizationReducedAccuracy, 1)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(CoreLocation.CLLocationManager.locationServicesEnabled)
        self.assertResultIsBOOL(CoreLocation.CLLocationManager.headingAvailable)
        self.assertResultIsBOOL(
            CoreLocation.CLLocationManager.significantLocationChangeMonitoringAvailable
        )
        self.assertResultIsBOOL(
            CoreLocation.CLLocationManager.regionMonitoringAvailable
        )
        self.assertResultIsBOOL(CoreLocation.CLLocationManager.regionMonitoringEnabled)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(
            CoreLocation.CLLocationManager.deferredLocationUpdatesAvailable
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(
            CoreLocation.CLLocationManager.isMonitoringAvailableForClass_
        )
        self.assertResultIsBOOL(CoreLocation.CLLocationManager.locationServicesEnabled)
        self.assertResultIsBOOL(
            CoreLocation.CLLocationManager.pausesLocationUpdatesAutomatically
        )
        self.assertArgIsBOOL(
            CoreLocation.CLLocationManager.setPausesLocationUpdatesAutomatically_, 0
        )
        self.assertResultIsBOOL(
            CoreLocation.CLLocationManager.allowsBackgroundLocationUpdates
        )
        self.assertArgIsBOOL(
            CoreLocation.CLLocationManager.setAllowsBackgroundLocationUpdates_, 0
        )
        self.assertResultIsBOOL(CoreLocation.CLLocationManager.headingAvailable)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(CoreLocation.CLLocationManager.isRangingAvailable)

    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            CoreLocation.CLLocationManager.isAuthorizedForWidgetUpdates
        )
        self.assertResultIsBOOL(
            CoreLocation.CLLocationManager.isAuthorizedForPreciseLocation
        )

        self.assertArgIsBlock(
            CoreLocation.CLLocationManager.requestTemporaryFullAccuracyAuthorizationWithPurposeKey_completion_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            CoreLocation.CLLocationManager.requestTemporaryPreciseLocationAuthorizationWithPurposeKey_completion_,
            1,
            b"v@",
        )
