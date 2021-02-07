import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLBeaconRegion(TestCase):
    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertResultIsBOOL(CoreLocation.CLBeaconRegion.notifyEntryStateOnDisplay)
        self.assertArgIsBOOL(
            CoreLocation.CLBeaconRegion.setNotifyEntryStateOnDisplay_, 0
        )
