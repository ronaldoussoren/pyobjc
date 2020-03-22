import SoundAnalysis
from PyObjCTools.TestSupport import TestCase


class TestSNError(TestCase):
    def test_constants(self):
        self.assertEqual(SoundAnalysis.SNErrorCodeUnknownError, 1)
        self.assertEqual(SoundAnalysis.SNErrorCodeOperationFailed, 2)
        self.assertEqual(SoundAnalysis.SNErrorCodeInvalidFormat, 3)
        self.assertEqual(SoundAnalysis.SNErrorCodeInvalidModel, 4)
        self.assertEqual(SoundAnalysis.SNErrorCodeInvalidFile, 5)
