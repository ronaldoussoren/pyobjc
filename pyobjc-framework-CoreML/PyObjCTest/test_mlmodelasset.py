from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreML


class TestMLModelAsset(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsOut(
            CoreML.MLModelAsset.modelAssetWithSpecificationData_error_, 1
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertArgIsOut(CoreML.MLModelAsset.modelAssetWithURL_error_, 1)

        self.assertArgIsBlock(
            CoreML.MLModelAsset.modelDescriptionWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            CoreML.MLModelAsset.modelDescriptionOfFunctionNamed_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            CoreML.MLModelAsset.functionNamesWithCompletionHandler_, 0, b"v@@"
        )
