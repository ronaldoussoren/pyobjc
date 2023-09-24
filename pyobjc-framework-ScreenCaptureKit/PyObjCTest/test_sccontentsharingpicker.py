from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import ScreenCaptureKit


class TestSCContentSharingPicker(TestCase):
    def test_constants(self):
        self.assertIsEnumType(ScreenCaptureKit.SCContentSharingPickerMode)
        self.assertEqual(
            ScreenCaptureKit.SCContentSharingPickerModeSingleWindow, 1 << 0
        )
        self.assertEqual(
            ScreenCaptureKit.SCContentSharingPickerModeMultipleWindows, 1 << 1
        )
        self.assertEqual(
            ScreenCaptureKit.SCContentSharingPickerModeSingleApplication, 1 << 2
        )
        self.assertEqual(
            ScreenCaptureKit.SCContentSharingPickerModeMultipleApplications, 1 << 3
        )
        self.assertEqual(
            ScreenCaptureKit.SCContentSharingPickerModeSingleDisplay, 1 << 4
        )

    @min_sdk_level("14.0")
    def test_protocols(self):
        self.assertProtocolExists("SCContentSharingPickerObserver")

    @min_os_level("14.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            ScreenCaptureKit.SCContentSharingPickerConfiguration.allowsChangingSelectedContent
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCContentSharingPickerConfiguration.setAllowsChangingSelectedContent_,
            0,
        )

        self.assertResultIsBOOL(ScreenCaptureKit.SCContentSharingPicker.isActive)
        self.assertArgIsBOOL(ScreenCaptureKit.SCContentSharingPicker.setActive_, 0)
