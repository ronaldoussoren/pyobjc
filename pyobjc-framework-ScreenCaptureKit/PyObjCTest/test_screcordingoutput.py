from PyObjCTools.TestSupport import TestCase, min_sdk_level

import ScreenCaptureKit  # noqa: F401


class TestSCRecordingOutput(TestCase):
    @min_sdk_level("15.0")
    def test_protocols(self):
        self.assertProtocolExists("SCRecordingOutputDelegate")
