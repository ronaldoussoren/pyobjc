import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLMonitorConfiguration(TestCase):
    @min_os_level("14.0")
    def testMethods14_0(self):
        self.assertResultIsBlock(
            CoreLocation.CLMonitorConfiguration.eventHandler, b"v@@"
        )
        self.assertArgIsBlock(
            CoreLocation.CLMonitorConfiguration.configWithMonitorName_queue_eventHandler_,
            2,
            b"v@@",
        )
