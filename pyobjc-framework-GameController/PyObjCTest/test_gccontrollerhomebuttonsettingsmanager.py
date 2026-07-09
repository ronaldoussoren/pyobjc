from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
)
import sys
import GameController

GCControllerHomeButtonSettingsDidChangeHandler = b"v@"


class TestGCControllerHomeButtonSettingsManager(TestCase):
    def test_enums(self):
        self.assertIsEnumType(GameController.GCControllerHomeButtonSettingSystemAction)
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingSystemActionUnavailable, -1
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingSystemActionOther, 0
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingSystemActionOpenCurrentApplication,
            1,
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingSystemActionDisabled,
            sys.maxsize,
        )

        self.assertIsEnumType(GameController.GCControllerHomeButtonSettingInAppAction)
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingInAppActionUnavailable, -1
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingInAppActionDefault, 0
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingInAppActionDefer, 1
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingInAppActionDisabled, sys.maxsize
        )

        self.assertIsEnumType(
            GameController.GCControllerHomeButtonSettingCustomizationStatus
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingCustomizationDefault, 0
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingCustomizationUser, 1
        )

        self.assertIsEnumType(
            GameController.GCControllerHomeButtonSettingsCustomizationActivity
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingsCustomizeSystemActionActivity,
            1,
        )
        self.assertEqual(
            GameController.GCControllerHomeButtonSettingsCustomizeInAppActionActivity, 2
        )

    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBlock(
            GameController.GCControllerHomeButtonSettingsManager.settingsDidChangeHandler,
            GCControllerHomeButtonSettingsDidChangeHandler,
        )
        self.assertArgIsBlock(
            GameController.GCControllerHomeButtonSettingsManager.setSettingsDidChangeHandler_,
            0,
            GCControllerHomeButtonSettingsDidChangeHandler,
        )

        self.assertResultIsBOOL(
            GameController.GCControllerHomeButtonSettingsManager.openControllerHomeButtonSettingsForActivity_error_
        )
        self.assertArgIsOut(
            GameController.GCControllerHomeButtonSettingsManager.openControllerHomeButtonSettingsForActivity_error_,
            1,
        )

        self.assertArgIsOut(
            GameController.GCControllerHomeButtonSettingsManager.readControllerHomeButtonSystemAction_withError_,
            1,
        )
        self.assertArgIsOut(
            GameController.GCControllerHomeButtonSettingsManager.readControllerHomeButtonSystemActionWithError_,
            0,
        )
        self.assertArgIsOut(
            GameController.GCControllerHomeButtonSettingsManager.readControllerHomeButtonInAppAction_withError_,
            1,
        )
        self.assertArgIsOut(
            GameController.GCControllerHomeButtonSettingsManager.readControllerHomeButtonInAppActionWithError_,
            0,
        )
