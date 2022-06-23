from PyObjCTools.TestSupport import (
    TestCase,
)
import GameController


class GCSyntheticDeviceKeys(TestCase):
    def test_constants(self):
        self.assertEqual(
            GameController.kIOHIDGCSyntheticDeviceKey, b"GCSyntheticDevice"
        )
