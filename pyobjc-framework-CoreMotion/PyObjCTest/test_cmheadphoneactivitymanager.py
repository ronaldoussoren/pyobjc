import CoreMotion
from PyObjCTools.TestSupport import TestCase, min_os_level

CMHeadphoneActivityStatusHandler = b"vq@"
CMHeadphoneActivityHandler = b"v@@"


class TestCMHeadphoneActivityManager(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreMotion.CMHeadphoneActivityStatus)
        self.assertEqual(CoreMotion.CMHeadphoneActivityStatusDisconnected, 0)
        self.assertEqual(CoreMotion.CMHeadphoneActivityStatusConnected, 1)

    @min_os_level("15.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            CoreMotion.CMHeadphoneActivityManager.isActivityAvailable
        )
        self.assertResultIsBOOL(CoreMotion.CMHeadphoneActivityManager.isActivityActive)
        self.assertResultIsBOOL(CoreMotion.CMHeadphoneActivityManager.isStatusAvailable)
        self.assertResultIsBOOL(CoreMotion.CMHeadphoneActivityManager.isStatusActive)

        self.assertArgIsBlock(
            CoreMotion.CMHeadphoneActivityManager.startActivityUpdatesToQueue_withHandler_,
            1,
            CMHeadphoneActivityHandler,
        )
        self.assertArgIsBlock(
            CoreMotion.CMHeadphoneActivityManager.startStatusUpdatesToQueue_withHandler_,
            1,
            CMHeadphoneActivityStatusHandler,
        )
