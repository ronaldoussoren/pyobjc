import CoreLocation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCLMonitor(TestCase):
    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsBlock(
            CoreLocation.CLMonitor.requestMonitorWithConfiguration_completion_, 1, b"v@"
        )
