import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLLocationUpdater(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreLocation.CLLiveUpdateConfiguration)
        self.assertEqual(CoreLocation.CLLiveUpdateConfigurationDefault, 0)
        self.assertEqual(CoreLocation.CLLiveUpdateConfigurationAutomotiveNavigation, 1)
        self.assertEqual(CoreLocation.CLLiveUpdateConfigurationOtherNavigation, 2)
        self.assertEqual(CoreLocation.CLLiveUpdateConfigurationFitness, 3)

    @min_os_level("14.0")
    def testMethods14_0(self):
        self.assertResultIsBOOL(CoreLocation.CLUpdate.isStationary)

        self.assertArgIsBlock(
            CoreLocation.CLLocationUpdater.liveUpdaterWithQueue_handler_, 1, b"v@"
        )
        self.assertArgIsBlock(
            CoreLocation.CLLocationUpdater.liveUpdaterWithConfiguration_queue_handler_,
            2,
            b"v@",
        )
