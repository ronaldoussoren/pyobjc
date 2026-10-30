from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level

import ScreenCaptureKit


class TestSCRecordingOutput(TestCase):
    @min_sdk_level("15.0")
    def test_protocols(self):
        self.assertProtocolExists("SCRecordingOutputDelegate", ScreenCaptureKit)

    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            ScreenCaptureKit.SCRecordingOutputConfiguration.mixesAudioWithMicrophone
        )
        self.assertArgIsBOOL(
            ScreenCaptureKit.SCRecordingOutputConfiguration.setMixesAudioWithMicrophone_,
            0,
        )
