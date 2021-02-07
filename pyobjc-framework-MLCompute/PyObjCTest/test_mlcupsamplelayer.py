from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCUpsampleLayer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCUpsampleLayer.alignsCorners)

        self.assertArgIsBOOL(
            MLCompute.MLCUpsampleLayer.layerWithShape_sampleMode_alignsCorners_, 2
        )
