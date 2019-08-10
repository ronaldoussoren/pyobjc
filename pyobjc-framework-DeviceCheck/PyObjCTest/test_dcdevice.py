import sys
from PyObjCTools.TestSupport import *

if sys.maxsize > 2 ** 32:
    import DeviceCheck

    class TestDCDevice(TestCase):
        @min_os_level("10.15")
        def test_methods(self):
            self.assertResultIsBOOL(DeviceCheck.DCDevice.isSupported)

            self.assertArgIsBlock(
                DeviceCheck.DCDevice.generateTokenWithCompletionHandler_, 0, b"v@@"
            )
