from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModelStructurePipeline(TestCase):
    @min_os_level("14.4")
    def test_classes(self):
        self.assertTrue(CoreML.MLModelStructurePipeline.__objc_final__)
