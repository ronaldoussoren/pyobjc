from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNCalculateImageAestheticsScoresRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNCalculateImageAestheticsScoresRequestRevision1, 1)
