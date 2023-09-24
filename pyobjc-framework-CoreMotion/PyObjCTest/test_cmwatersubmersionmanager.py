from PyObjCTools.TestSupport import TestCase, min_sdk_level

import CoreMotion  # noqa: F401


class TestCMWaterSubmersionManager(TestCase):
    @min_sdk_level("13.0")
    def test_protocols(self):
        self.assertProtocolExists("CMWaterSubmersionManagerDelegate")
