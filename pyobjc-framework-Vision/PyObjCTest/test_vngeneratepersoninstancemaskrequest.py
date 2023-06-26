from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNGeneratePersonInstanceMaskRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNGeneratePersonInstanceMaskRequestRevision1, 1)
