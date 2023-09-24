import CoreMotion
from PyObjCTools.TestSupport import TestCase, min_os_level

CMHeadphoneDeviceMotionHandler = b"v@@"


class TestCMHeadphoneMotionManager(TestCase):
    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            CoreMotion.CMHeadphoneMotionManager.isDeviceMotionAvailable
        )
        self.assertResultIsBOOL(
            CoreMotion.CMHeadphoneMotionManager.isDeviceMotionActive
        )
        self.assertArgIsBlock(
            CoreMotion.CMHeadphoneMotionManager.startDeviceMotionUpdatesToQueue_withHandler_,
            1,
            CMHeadphoneDeviceMotionHandler,
        )
