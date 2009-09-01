
from PyObjCTools.TestSupport import *
from CoreLocation import *

class TestCLLocation (TestCase):

    @min_os_level('10.6')
    def testTypes(self):
        v = CLLocationCoordinate2D()
        self.failUnlessIsInstance(v.latitude, float)
        self.failUnlessIsInstance(v.longitude, float)
        self.failUnlessEqual(CLLocationCoordinate2D.__typestr__,
                '{_CLLocationCoordinate2D=dd}')


    @min_os_level('10.6')
    def testConstants(self):
        self.failUnlessIsInstance(kCLDistanceFilterNone, float)

        self.failUnlessIsInstance(kCLLocationAccuracyBest, float)
        self.failUnlessIsInstance(kCLLocationAccuracyNearestTenMeters, float)
        self.failUnlessIsInstance(kCLLocationAccuracyHundredMeters, float)
        self.failUnlessIsInstance(kCLLocationAccuracyKilometer, float)
        self.failUnlessIsInstance(kCLLocationAccuracyThreeKilometers, float)

    @min_os_level('10.6')
    def testMethods(self):
        self.failUnlessResultHasType(CLLocation.coordinate, CLLocationCoordinate2D.__typestr__)
        #self.failUnlessArgHasType(CLLocation.setCoordinate_, 0, CLLocationCoordinate2D.__typestr__)

        self.failUnlessArgHasType(CLLocation.initWithCoordinate_altitude_horizontalAccuracy_verticalAccuracy_timestamp_, 0,
                CLLocationCoordinate2D.__typestr__)


if __name__ == "__main__":
    main()
