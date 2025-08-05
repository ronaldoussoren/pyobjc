import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestVTMotionEstimationSessionProperties(TestCase):
    @min_os_level("26.0")
    def test_constants(self):
        self.assertIsInstance(
            VideoToolbox.kVTMotionEstimationSessionCreationOption_MotionVectorSize, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTMotionEstimationSessionCreationOption_UseMultiPassSearch,
            str,
        )
        self.assertIsInstance(
            VideoToolbox.kVTMotionEstimationSessionCreationOption_DetectTrueMotion, str
        )
        self.assertIsInstance(
            VideoToolbox.kVTMotionEstimationSessionCreationOption_Label, str
        )
