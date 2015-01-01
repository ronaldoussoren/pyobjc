from PyObjCTools.TestSupport import *
from CoreLocation import *


class TestCLRegion (TestCase):
    def testConstants(self):
        self.assertEqual(CLRegionStateUnknown, 0)
        self.assertEqual(CLRegionStateInside, 1)
        self.assertEqual(CLRegionStateOutside, 2)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(CLRegion.containsCoordinate_)
        self.assertArgHasType(CLRegion.containsCoordinate_, 0, CLLocationCoordinate2D.__typestr__)

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(CLRegion.notifyOnEntry)
        self.assertArgIsBOOL(CLRegion.setNotifyOnEntry_, 0)
        self.assertResultIsBOOL(CLRegion.notifyOnExit)
        self.assertArgIsBOOL(CLRegion.setNotifyOnExit_, 0)

if __name__ == "__main__":
    main()
