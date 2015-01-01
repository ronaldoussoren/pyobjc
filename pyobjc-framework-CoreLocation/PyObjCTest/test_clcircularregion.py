from PyObjCTools.TestSupport import *
from CoreLocation import *


class TestCLCircularRegion (TestCase):

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(CLCircularRegion.containsCoordinate_)
        self.assertArgHasType(CLCircularRegion.containsCoordinate_, 0, CLLocationCoordinate2D.__typestr__)

        self.assertResultHasType(CLCircularRegion.center, CLLocationCoordinate2D.__typestr__)

if __name__ == "__main__":
    main()
