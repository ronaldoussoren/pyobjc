from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)
import GameController


class TestGCDirectionalGamepad(TestCase):
    @min_os_level("11.3")
    def testConstants11_3(self):
        self.assertIsInstance(GameController.GCInputDirectionalDpad, str)
        self.assertIsInstance(GameController.GCInputDirectionalCardinalDpad, str)
