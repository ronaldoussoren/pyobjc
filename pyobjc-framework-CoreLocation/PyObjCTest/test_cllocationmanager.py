
from PyObjCTools.TestSupport import *
from CoreLocation import *

class TestCLLocationManager (TestCase):
    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(CLLocationManager.alloc().init().locationServicesEnabled)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(CLDeviceOrientationUnknown, 0)
        self.assertEqual(CLDeviceOrientationPortrait, 1)
        self.assertEqual(CLDeviceOrientationPortraitUpsideDown, 2)
        self.assertEqual(CLDeviceOrientationLandscapeLeft, 3)
        self.assertEqual(CLDeviceOrientationLandscapeRight, 4)
        self.assertEqual(CLDeviceOrientationFaceUp, 5)
        self.assertEqual(CLDeviceOrientationFaceDown, 6)

        self.assertEqual(kCLAuthorizationStatusNotDetermined, 0)
        self.assertEqual(kCLAuthorizationStatusRestricted, 1)
        self.assertEqual(kCLAuthorizationStatusDenied, 2)
        self.assertEqual(kCLAuthorizationStatusAuthorizedAlways, 3)
        self.assertEqual(kCLAuthorizationStatusAuthorized, kCLAuthorizationStatusAuthorizedAlways)

        self.assertEqual(CLActivityTypeOther, 1)
        self.assertEqual(CLActivityTypeAutomotiveNavigation, 2)
        self.assertEqual(CLActivityTypeFitness, 3)
        self.assertEqual(CLActivityTypeOtherNavigation, 4)
        self.assertEqual(CLActivityTypeAirborne, 5)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(CLLocationManager.locationServicesEnabled)
        self.assertResultIsBOOL(CLLocationManager.headingAvailable)
        self.assertResultIsBOOL(CLLocationManager.significantLocationChangeMonitoringAvailable)
        self.assertResultIsBOOL(CLLocationManager.regionMonitoringAvailable)
        self.assertResultIsBOOL(CLLocationManager.regionMonitoringEnabled)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(CLLocationManager.deferredLocationUpdatesAvailable)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(CLLocationManager.isMonitoringAvailableForClass_)

if __name__ == "__main__":
    main()
