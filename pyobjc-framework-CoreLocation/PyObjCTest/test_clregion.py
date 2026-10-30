import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLRegion(TestCase):
    def test_enums(self):
        self.assertIsEnumType(CoreLocation.CLRegionState)
        self.assertEqual(CoreLocation.CLRegionStateUnknown, 0)
        self.assertEqual(CoreLocation.CLRegionStateInside, 1)
        self.assertEqual(CoreLocation.CLRegionStateOutside, 2)

        self.assertIsEnumType(CoreLocation.CLProximity)
        self.assertEqual(CoreLocation.CLProximityUnknown, 0)
        self.assertEqual(CoreLocation.CLProximityImmediate, 1)
        self.assertEqual(CoreLocation.CLProximityNear, 2)
        self.assertEqual(CoreLocation.CLProximityFar, 3)

    def test_methods(self):
        self.assertResultIsBOOL(CoreLocation.CLRegion.containsCoordinate_)
        self.assertArgHasType(
            CoreLocation.CLRegion.containsCoordinate_,
            0,
            CoreLocation.CLLocationCoordinate2D.__typestr__,
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(CoreLocation.CLRegion.notifyOnEntry)
        self.assertArgIsBOOL(CoreLocation.CLRegion.setNotifyOnEntry_, 0)
        self.assertResultIsBOOL(CoreLocation.CLRegion.notifyOnExit)
        self.assertArgIsBOOL(CoreLocation.CLRegion.setNotifyOnExit_, 0)
