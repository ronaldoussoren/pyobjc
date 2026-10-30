import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVSampleBufferAudioRenderer(TestCase):
    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVSampleBufferAudioRenderer.isMuted
        )  # noqa: B950
        self.assertArgIsBOOL(
            AVFoundation.AVSampleBufferAudioRenderer.setMuted_, 0
        )  # noqa: B950

        self.assertArgIsBlock(
            AVFoundation.AVSampleBufferAudioRenderer.flushFromSourceTime_completionHandler_,  # noqa: B950
            1,
            b"vZ",
        )

    @min_os_level("10.13")
    def test_constants10_13(self):
        self.assertIsInstance(
            AVFoundation.AVSampleBufferAudioRendererWasFlushedAutomaticallyNotification,  # noqa: B950
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVSampleBufferAudioRendererFlushTimeKey, str
        )  # noqa: B950

    @min_os_level("12.0")
    def test_constants12_0(self):
        self.assertIsInstance(
            AVFoundation.AVSampleBufferAudioRendererOutputConfigurationDidChangeNotification,  # noqa: B950
            str,
        )
