from PyObjCTools.TestSupport import TestCase, min_os_level

import CoreML


class TestMLModelAsset(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsOut(
            CoreML.MLModelAsset.modelAssetWithSpecificationData_error_, 1
        )
