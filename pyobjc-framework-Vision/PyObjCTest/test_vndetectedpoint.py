from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNClassifyImageRequest(TestCase):
    @min_os_level("10.16")
    def test_constants10_16(self):
        self.assertEqual(Vision.VNRecognizedPointKey, str)
        self.assertEqual(Vision.VNRecognizedPointGroupKey, str)
