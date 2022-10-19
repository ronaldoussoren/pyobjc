from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level

import CoreMotion


class TestCMWaterSubmersionManager(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("CMWaterSubmersionManagerDelegate")

    @min_os_level("13.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            CoreMotion.CMWaterSubmersionManager.waterSubmersionAvailable
        )
