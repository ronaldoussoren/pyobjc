
from PyObjCTools.TestSupport import *
from CoreLocation import *

class TestCLLocation (TestCase):

    @min_os_level('10.6')
    def testTypes(self):
        v = CLLocationCoordinate2D()
        self.assertIsInstance(v.latitude, float)
        self.assertIsInstance(v.longitude, float)
        self.assertEqual(CLLocationCoordinate2D.__typestr__,
                b'{_CLLocationCoordinate2D=dd}')


    @min_os_level('10.6')
    def testConstants(self):
        self.assertIsInstance(kCLDistanceFilterNone, float)

        self.assertIsInstance(kCLLocationAccuracyBest, float)
        self.assertIsInstance(kCLLocationAccuracyNearestTenMeters, float)
        self.assertIsInstance(kCLLocationAccuracyHundredMeters, float)
        self.assertIsInstance(kCLLocationAccuracyKilometer, float)
        self.assertIsInstance(kCLLocationAccuracyThreeKilometers, float)

    @min_os_level('10.7')
    def testConstants10_7(self):
        self.assertIsInstance(kCLLocationAccuracyBestForNavigation, float)
        self.assertIsInstance(kCLLocationCoordinate2DInvalid, CLLocationCoordinate2D)

    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultHasType(CLLocation.coordinate, CLLocationCoordinate2D.__typestr__)
        #self.assertArgHasType(CLLocation.setCoordinate_, 0, CLLocationCoordinate2D.__typestr__)

        self.assertArgHasType(CLLocation.initWithCoordinate_altitude_horizontalAccuracy_verticalAccuracy_timestamp_, 0,
                CLLocationCoordinate2D.__typestr__)

    @min_os_level('10.7')
    def testFunctions10_7(self):
        self.assertResultIsBOOL(CLLocationCoordinate2DIsValid)
        self.assertFalse(CLLocationCoordinate2DIsValid(kCLLocationCoordinate2DInvalid))

        loc = CLLocationCoordinate2DMake(0.0, 0.0)
        self.assertIsInstance(loc, CLLocationCoordinate2D)

        self.assertTrue(CLLocationCoordinate2DIsValid(loc))

if __name__ == "__main__":
    main()
