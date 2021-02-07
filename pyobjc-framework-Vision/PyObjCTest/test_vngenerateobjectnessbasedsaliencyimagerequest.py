from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNGenerateObjectnessBasedSaliencyImageRequest(TestCase):
    def test_constants(self):
        self.assertEqual(
            Vision.VNGenerateObjectnessBasedSaliencyImageRequestRevision1, 1
        )
