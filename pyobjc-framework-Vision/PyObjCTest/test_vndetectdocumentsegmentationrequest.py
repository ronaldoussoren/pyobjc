from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNDetectDocumentSegmentationRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNDetectDocumentSegmentationRequestRevision1, 1)
