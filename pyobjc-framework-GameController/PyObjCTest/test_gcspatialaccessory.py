from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)
import GameController


class TestGCAxisElement(TestCase):
    @min_os_level("27.0")
    def tesT_constants(self):
        self.assertIsInstance(
            GameController.GCSpatialAccessoryDidConnectNotification, str
        )
        self.assertIsInstance(
            GameController.GCSpatialAccessoryDidDisconnectNotification, str
        )

    @min_os_level("27.0")
    def tesT_methods(self):
        self.assertResultIsBOOL(GameController.GCSpatialAccessory.conformsToDeviceType_)
