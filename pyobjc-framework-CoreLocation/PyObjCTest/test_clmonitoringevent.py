import CoreLocation
from PyObjCTools.TestSupport import TestCase


class TestCLMonitoringEvent(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreLocation.CLMonitoringState)
        self.assertEqual(CoreLocation.CLMonitoringStateUnknown, 0)
        self.assertEqual(CoreLocation.CLMonitoringStateSatisfied, 1)
        self.assertEqual(CoreLocation.CLMonitoringStateUnsatisfied, 2)
        self.assertEqual(CoreLocation.CLMonitoringStateUnmonitored, 3)
