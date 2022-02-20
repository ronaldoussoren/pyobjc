from PyObjCTools.TestSupport import TestCase
import CoreML


class TestMLUpdateProgressEvent(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreML.MLUpdateProgressEvent)

    def test_constants(self):
        self.assertEqual(CoreML.MLUpdateProgressEventTrainingBegin, 1 << 0)
        self.assertEqual(CoreML.MLUpdateProgressEventEpochEnd, 1 << 1)
        self.assertEqual(CoreML.MLUpdateProgressEventMiniBatchEnd, 1 << 2)
