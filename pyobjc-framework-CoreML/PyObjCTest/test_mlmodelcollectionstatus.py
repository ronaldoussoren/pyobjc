from PyObjCTools.TestSupport import TestCase
import CoreML


class TestMLModelCollectionStatus(TestCase):
    def test_constants(self):
        self.assertEqual(CoreML.MLModelCollectionStatusCouldNotDetermine, 0)
        self.assertEqual(CoreML.MLModelCollectionStatusSyncing, 1)
        self.assertEqual(CoreML.MLModelCollectionStatusReady, 2)
