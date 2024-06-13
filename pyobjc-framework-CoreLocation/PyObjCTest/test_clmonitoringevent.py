import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLMonitoringEvent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreLocation.CLMonitoringState)
        self.assertEqual(CoreLocation.CLMonitoringStateUnknown, 0)
        self.assertEqual(CoreLocation.CLMonitoringStateSatisfied, 1)
        self.assertEqual(CoreLocation.CLMonitoringStateUnsatisfied, 2)
        self.assertEqual(CoreLocation.CLMonitoringStateUnmonitored, 3)

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(CoreLocation.CLMonitoringEvent.authorizationDenied)
        self.assertResultIsBOOL(
            CoreLocation.CLMonitoringEvent.authorizationDeniedGlobally
        )
        self.assertResultIsBOOL(CoreLocation.CLMonitoringEvent.authorizationRestricted)
        self.assertResultIsBOOL(CoreLocation.CLMonitoringEvent.insufficientlyInUse)
        self.assertResultIsBOOL(CoreLocation.CLMonitoringEvent.accuracyLimited)
        self.assertResultIsBOOL(CoreLocation.CLMonitoringEvent.conditionUnsupported)
        self.assertResultIsBOOL(CoreLocation.CLMonitoringEvent.conditionLimitExceeded)
        self.assertResultIsBOOL(CoreLocation.CLMonitoringEvent.persistenceUnavailable)
        self.assertResultIsBOOL(CoreLocation.CLMonitoringEvent.serviceSessionRequired)
        self.assertResultIsBOOL(
            CoreLocation.CLMonitoringEvent.authorizationRequestInProgress
        )
