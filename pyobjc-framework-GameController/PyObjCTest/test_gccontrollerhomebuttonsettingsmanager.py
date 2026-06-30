from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)
import sys
import GameController


class TestGCControllerHomeButtonSettingsManager(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameController.GCControllerHomeButtonSettingsAction)
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingsActionUnavailable, 0
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingsActionOpenCurrentApplication, 1
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingsActionOther, sys.maxsize
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingsActionDisabled, -1
        )

        self.assertIsEnumType(GameController.GCControllerHomeButtonSettingsActivity)
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingsCustomizeActionActivity, 1
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingsCustomizeOverridesActivity, 2
        )

    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            GameController.GCControllerHomeButtonSettingsManager.openControllerHomeButtonSettingsForActivity_error_
        )
        self.assertArgIsOut(
            GameController.GCControllerHomeButtonSettingsManager.openControllerHomeButtonSettingsForActivity_error_,
            1,
        )

        self.assertArgIsOut(
            GameController.GCControllerHomeButtonSettingsManager.readControllerHomeButtonActionWithError_,
            0,
        )
