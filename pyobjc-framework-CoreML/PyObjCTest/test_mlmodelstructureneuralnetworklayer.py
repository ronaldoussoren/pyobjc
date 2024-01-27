from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModelStructureNeuralNetworkLayer(TestCase):
    @min_os_level("14.4")
    def test_classes(self):
        self.assertFalse(CoreML.MLModelStructureNeuralNetworkLayer.__objc_final__)
