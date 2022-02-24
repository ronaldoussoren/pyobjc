import os

import CoreLocation
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    os_level_key,
    expectedFailureIf,
)


class TestCLError(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreLocation.CLError)

    @min_os_level("10.6")
    def testConstants(self):
        self.assertIsInstance(CoreLocation.kCLErrorDomain, str)

        self.assertEqual(CoreLocation.kCLErrorLocationUnknown, 0)
        self.assertEqual(CoreLocation.kCLErrorDenied, 1)
        self.assertEqual(CoreLocation.kCLErrorNetwork, 2)
        self.assertEqual(CoreLocation.kCLErrorHeadingFailure, 3)
        self.assertEqual(CoreLocation.kCLErrorRegionMonitoringDenied, 4)
        self.assertEqual(CoreLocation.kCLErrorRegionMonitoringFailure, 5)
        self.assertEqual(CoreLocation.kCLErrorRegionMonitoringSetupDelayed, 6)
        self.assertEqual(CoreLocation.kCLErrorRegionMonitoringResponseDelayed, 7)
        self.assertEqual(CoreLocation.kCLErrorGeocodeFoundPartialResult, 9)
        self.assertEqual(CoreLocation.kCLErrorDeferredFailed, 11)
        self.assertEqual(CoreLocation.kCLErrorDeferredNotUpdatingLocation, 12)
        self.assertEqual(CoreLocation.kCLErrorDeferredAccuracyTooLow, 13)
        self.assertEqual(CoreLocation.kCLErrorDeferredDistanceFiltered, 14)
        self.assertEqual(CoreLocation.kCLErrorDeferredCanceled, 15)
        self.assertEqual(CoreLocation.kCLErrorRangingUnavailable, 16)
        self.assertEqual(CoreLocation.kCLErrorRangingFailure, 17)
        self.assertEqual(CoreLocation.kCLErrorPromptDeclined, 18)

        if int(os.uname()[2].split(".")[0]) < 12:
            self.assertEqual(CoreLocation.kCLErrorGeocodeFoundNoResult, 7)
            self.assertEqual(CoreLocation.kCLErrorGeocodeCanceled, 8)
        else:
            self.assertEqual(CoreLocation.kCLErrorGeocodeFoundNoResult, 8)
            self.assertEqual(CoreLocation.kCLErrorGeocodeCanceled, 10)

    @min_os_level("10.7")
    @expectedFailureIf(os_level_key(os_release()) < os_level_key("10.13"))
    def testConstants10_7(self):
        self.assertIsInstance(CoreLocation.kCLErrorUserInfoAlternateRegionKey, str)
