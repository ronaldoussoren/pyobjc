from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import Virtualization


class TestVZGraphicsDisplay(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            Virtualization.VZGraphicsDisplay.reconfigureWithSizeInPixels_error_
        )
        self.assertArgIsOut(
            Virtualization.VZGraphicsDisplay.reconfigureWithSizeInPixels_error_, 1
        )

        self.assertResultIsBOOL(
            Virtualization.VZGraphicsDisplay.reconfigureWithConfiguration_error_
        )
        self.assertArgIsOut(
            Virtualization.VZGraphicsDisplay.reconfigureWithConfiguration_error_, 1
        )

    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("VZGraphicsDisplayObserver")
