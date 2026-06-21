from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import ScreenCaptureKit


class TestSCRecordingEditor(TestCase):
    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("SCRecordingEditorDelegate", ScreenCaptureKit)

    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsBlock(
            ScreenCaptureKit.SCRecordingEditor.presentFromWindow_completionHandler_,
            1,
            b"v@",
        )
        self.assertArgIsBlock(
            ScreenCaptureKit.SCRecordingEditor.presentFromWindow_mode_completionHandler_,
            2,
            b"v@",
        )
