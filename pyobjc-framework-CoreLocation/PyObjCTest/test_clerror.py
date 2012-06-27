
from PyObjCTools.TestSupport import *
from CoreLocation import *
import os

try:
    unicode
except NameError:
    unicode = str

class TestCLError (TestCase):
    @min_os_level('10.6')
    def testConstants(self):
        self.assertIsInstance(kCLErrorDomain, unicode)

        self.assertEqual(kCLErrorLocationUnknown, 0)
        self.assertEqual(kCLErrorDenied, 1)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertEqual(kCLErrorNetwork, 2)
        self.assertEqual(kCLErrorHeadingFailure, 3)
        self.assertEqual(kCLErrorRegionMonitoringDenied, 4)
        self.assertEqual(kCLErrorRegionMonitoringFailure, 5)
        self.assertEqual(kCLErrorRegionMonitoringSetupDelayed, 6)

        if int(os.uname()[2].split('.')[0]) < 12:
            self.assertEqual(kCLErrorFoundNoResult, 7)
            self.assertEqual(kCLErrorCanceled, 8)

    @min_os_level('10.8')
    def testConstants10_8(self):
        self.assertEqual(kCLErrorRegionMonitoringResponseDelayed, 7)
        self.assertEqual(kCLErrorGeocodeFoundNoResult, 8)
        self.assertEqual(kCLErrorGeocodeFoundPartialResult, 9)
        self.assertEqual(kCLErrorGeocodeCanceled, 10)

if __name__ == "__main__":
    main()
