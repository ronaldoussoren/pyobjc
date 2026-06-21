from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import ScreenCaptureKit


class TestSCClipBufferingOutput(TestCase):
    @min_sdk_level("27.0")
    def test_protocols(self):
        self.assertProtocolExists("SCClipBufferingOutputDelegate", ScreenCaptureKit)

    @min_os_level("27.0")
    def test_methods(self):
        self.assertArgIsBlock(
            ScreenCaptureKit.SCClipBufferingOutput.exportClipToURL_duration_completionHandler_,
            2,
            b"v@",
        )
