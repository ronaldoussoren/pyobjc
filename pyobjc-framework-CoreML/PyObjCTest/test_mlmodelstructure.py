from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLModelStructure(TestCase):
    @min_os_level("14.4")
    def test_classes(self):
        self.assertFalse(CoreML.MLModelStructure.__objc_final__)

        self.assertArgIsBlock(
            CoreML.MLModelStructure.loadContentsOfURL_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            CoreML.MLModelStructure.loadModelAsset_completionHandler_, 1, b"v@@"
        )
