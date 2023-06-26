import CoreMotion  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestCMHeadphoneMotionManagerDelegate(TestCase):
    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("CMHeadphoneMotionManagerDelegate")
