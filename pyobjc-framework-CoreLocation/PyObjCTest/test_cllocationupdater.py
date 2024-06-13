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

    @min_os_level("15.0")
    def testMethods15_0(self):
        self.assertResultIsBOOL(CoreLocation.CLUpdate.authorizationDenied)
        self.assertResultIsBOOL(CoreLocation.CLUpdate.authorizationDeniedGlobally)
        self.assertResultIsBOOL(CoreLocation.CLUpdate.authorizationRestricted)
        self.assertResultIsBOOL(CoreLocation.CLUpdate.stationary)
        self.assertResultIsBOOL(CoreLocation.CLUpdate.insufficientlyInUse)
        self.assertResultIsBOOL(CoreLocation.CLUpdate.locationUnavailable)
        self.assertResultIsBOOL(CoreLocation.CLUpdate.accuracyLimited)
        self.assertResultIsBOOL(CoreLocation.CLUpdate.serviceSessionRequired)
        self.assertResultIsBOOL(CoreLocation.CLUpdate.authorizationRequestInProgress)
