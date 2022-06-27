from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)
import GameController


class TestGCRacingWheel(TestCase):
    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(GameController.GCRacingWheelDidConnectNotification, str)
        self.assertIsInstance(
            GameController.GCRacingWheelDidDisconnectNotification, str
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(GameController.GCRacingWheel.acquireDeviceWithError_)
        self.assertArgIsOut(GameController.GCRacingWheel.acquireDeviceWithError_, 0)

        self.assertResultIsBOOL(GameController.GCRacingWheel.isAcquired)
        self.assertResultIsBOOL(GameController.GCRacingWheel.isSnapshot)
