import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLCircularRegion(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(CoreLocation.CLCircularRegion.containsCoordinate_)
        self.assertArgHasType(
            CoreLocation.CLCircularRegion.containsCoordinate_,
            0,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )

        self.assertResultHasType(
            CoreLocation.CLCircularRegion.center,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )
