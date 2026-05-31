from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNGenerateForegroundInstanceMaskRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNGenerateForegroundInstanceMaskRequestRevision1, 1)
