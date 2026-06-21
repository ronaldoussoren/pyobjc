from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLComputePlan(TestCase):
    @min_os_level("14.4")
    def test_classes(self):
        self.assertTrue(CoreML.MLComputePlan.__objc_final__)

    @min_os_level("14.4")
    def test_methods(self):
        self.assertArgIsBlock(
            CoreML.MLComputePlan.loadContentsOfURL_configuration_completionHandler_,
            2,
            b"v@@",
        )
        self.assertArgIsBlock(
            CoreML.MLComputePlan.loadModelAsset_configuration_completionHandler_,
            2,
            b"v@@",
        )
