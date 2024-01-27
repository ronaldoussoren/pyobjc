from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModelStructure(TestCase):
    @min_os_level("14.4")
    def test_classes(self):
        self.assertFalse(CoreML.MLModelStructure.__objc_final__)

        self.assertArgIsOut(
            CoreML.MLModelStructure.modelStructureOfModelAtURL_error_, 1
        )
