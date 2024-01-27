from PyObjCTools.TestSupport import TestCase
import CoreML


class TestMLReshapeFrequencyHint(TestCase):
    def test_constants(self):
        self.assertIsEnumType(CoreML.MLReshapeFrequencyHint)
        self.assertEqual(CoreML.MLReshapeFrequencyHintFrequent, 0)
        self.assertEqual(CoreML.MLReshapeFrequencyHintInfrequent, 1)
