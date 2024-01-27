from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModelStructureNeuralNetwork(TestCase):
    @min_os_level("14.4")
    def test_classes(self):
        self.assertTrue(CoreML.MLModelStructureNeuralNetwork.__objc_final__)
