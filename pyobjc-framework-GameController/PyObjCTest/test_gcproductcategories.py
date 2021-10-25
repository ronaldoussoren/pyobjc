from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)
import GameController


class TestGCProductCategories(TestCase):
    @min_os_level("12.0")
    def test_constants(self):
        self.assertIsInstance(GameController.GCProductCategoryDualSense, str)
        self.assertIsInstance(GameController.GCProductCategoryDualShock4, str)
        self.assertIsInstance(GameController.GCProductCategoryMFi, str)
        self.assertIsInstance(GameController.GCProductCategoryXboxOne, str)

        self.assertIsInstance(GameController.GCProductCategorySiriRemote1stGen, str)

        self.assertIsInstance(GameController.GCProductCategorySiriRemote2ndGen, str)

        self.assertIsInstance(GameController.GCProductCategoryControlCenterRemote, str)

        self.assertIsInstance(
            GameController.GCProductCategoryUniversalElectronicsRemote, str
        )

        self.assertIsInstance(GameController.GCProductCategoryCoalescedRemote, str)

        self.assertIsInstance(GameController.GCProductCategoryMouse, str)
        self.assertIsInstance(GameController.GCProductCategoryKeyboard, str)
