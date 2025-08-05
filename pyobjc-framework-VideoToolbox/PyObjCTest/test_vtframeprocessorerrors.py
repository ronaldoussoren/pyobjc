import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTFrameProcessorErrors(TestCase):
    def test_constants(self):
        self.assertIsEnumType(VideoToolbox.VTFrameProcessorError)
        self.assertEqual(VideoToolbox.VTFrameProcessorUnknownError, -19730)
        self.assertEqual(VideoToolbox.VTFrameProcessorUnsupportedResolution, -19731)
        self.assertEqual(VideoToolbox.VTFrameProcessorSessionNotStarted, -19732)
        self.assertEqual(VideoToolbox.VTFrameProcessorSessionAlreadyActive, -19733)
        self.assertEqual(VideoToolbox.VTFrameProcessorFatalError, -19734)
        self.assertEqual(VideoToolbox.VTFrameProcessorSessionLevelError, -19735)
        self.assertEqual(VideoToolbox.VTFrameProcessorInitializationFailed, -19736)
        self.assertEqual(VideoToolbox.VTFrameProcessorUnsupportedInput, -19737)
        self.assertEqual(VideoToolbox.VTFrameProcessorMemoryAllocationFailure, -19738)
        self.assertEqual(VideoToolbox.VTFrameProcessorRevisionNotSupported, -19739)
        self.assertEqual(VideoToolbox.VTFrameProcessorProcessingError, -19740)
        self.assertEqual(VideoToolbox.VTFrameProcessorInvalidParameterError, -19741)
        self.assertEqual(VideoToolbox.VTFrameProcessorInvalidFrameTiming, -19742)
        self.assertEqual(VideoToolbox.VTFrameProcessorAssetDownloadFailed, -19743)

    @min_os_level("15.4")
    def test_constants15_4(self):
        self.assertIsInstance(VideoToolbox.VTFrameProcessorErrorDomain, str)
