from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNGenerateAttentionBasedSaliencyImageRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNGenerateAttentionBasedSaliencyImageRequestRevision1, 1)
        self.assertEqual(Vision.VNGenerateAttentionBasedSaliencyImageRequestRevision2, 2)
