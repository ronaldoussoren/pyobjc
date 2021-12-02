import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLLocation(TestCase):
    @min_os_level("10.6")
    def testStructs(self):
        v = CoreLocation.CLLocationCoordinate2D()
        self.assertIsInstance(v.latitude, float)
        self.assertIsInstance(v.longitude, float)
        self.assertPickleRoundTrips(v)
        self.assertEqual(
            CoreLocation.CLLocationCoordinate2D.__typestr__,
            b"{CLLocationCoordinate2D=dd}",
        )

    @min_os_level("10.6")
    def testConstants(self):
        self.assertIsInstance(CoreLocation.kCLDistanceFilterNone, float)

        self.assertIsInstance(CoreLocation.kCLLocationAccuracyBest, float)
        self.assertIsInstance(CoreLocation.kCLLocationAccuracyNearestTenMeters, float)
        self.assertIsInstance(CoreLocation.kCLLocationAccuracyHundredMeters, float)
        self.assertIsInstance(CoreLocation.kCLLocationAccuracyKilometer, float)
        self.assertIsInstance(CoreLocation.kCLLocationAccuracyThreeKilometers, float)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(CoreLocation.kCLLocationAccuracyBestForNavigation, float)
        self.assertIsInstance(
            CoreLocation.kCLLocationCoordinate2DInvalid,
            CoreLocation.CLLocationCoordinate2D,
        )

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(CoreLocation.CLLocationDistanceMax, float)
        self.assertIsInstance(CoreLocation.CLTimeIntervalMax, float)

    @min_os_level("11.0")
    def testConstants11_0(self):
        self.assertIsInstance(CoreLocation.kCLLocationAccuracyReduced, float)

    @min_os_level("10.6")
    def testMethods(self):
        self.assertResultHasType(
            CoreLocation.CLLocation.coordinate,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )
        # self.assertArgHasType(CoreLocation.CLLocation.setCoordinate_, 0, CoreLocation.CLLocationCoordinate2D.__typestr__)

        self.assertArgHasType(
            CoreLocation.CLLocation.initWithCoordinate_altitude_horizontalAccuracy_verticalAccuracy_timestamp_,
            0,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertArgIsBOOL(
            CoreLocation.CLLocationSourceInformation.initWithSoftwareSimulationState_andExternalAccessoryState_,
            1,
        )

        self.assertResultIsBOOL(
            CoreLocation.CLLocationSourceInformation.isSimulatedBySoftware
        )
        self.assertResultIsBOOL(
            CoreLocation.CLLocationSourceInformation.isProducedByAccessory
        )

    @min_os_level("10.7")
    def testFunctions10_7(self):
        self.assertResultIsBOOL(CoreLocation.CLLocationCoordinate2DIsValid)
        self.assertFalse(
            CoreLocation.CLLocationCoordinate2DIsValid(
                CoreLocation.kCLLocationCoordinate2DInvalid
            )
        )

        loc = CoreLocation.CLLocationCoordinate2DMake(0.0, 0.0)
        self.assertIsInstance(loc, CoreLocation.CLLocationCoordinate2D)

        self.assertTrue(CoreLocation.CLLocationCoordinate2DIsValid(loc))
