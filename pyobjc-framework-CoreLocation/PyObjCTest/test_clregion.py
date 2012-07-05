from PyObjCTools.TestSupport import *
from CoreLocation import *


class TestCLRegion (TestCase):

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(CLRegion.containsCoordinate_)
        self.assertArgHasType(CLRegion.containsCoordinate_, 0, CLLocationCoordinate2D.__typestr__)

if __name__ == "__main__":
    main()
