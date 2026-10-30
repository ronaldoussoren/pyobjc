from PyObjCTools.TestSupport import TestCase
import Vision


class TestVNDetectedPoint(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(Vision.VNRecognizedPointGroupKey, str)
        self.assertIsTypedEnum(Vision.VNRecognizedPointKey, str)
