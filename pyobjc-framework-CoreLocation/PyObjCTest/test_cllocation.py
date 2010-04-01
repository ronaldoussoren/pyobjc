
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

    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultHasType(CLLocation.coordinate, CLLocationCoordinate2D.__typestr__)
        #self.assertArgHasType(CLLocation.setCoordinate_, 0, CLLocationCoordinate2D.__typestr__)

        self.assertArgHasType(CLLocation.initWithCoordinate_altitude_horizontalAccuracy_verticalAccuracy_timestamp_, 0,
                CLLocationCoordinate2D.__typestr__)


if __name__ == "__main__":
    main()
