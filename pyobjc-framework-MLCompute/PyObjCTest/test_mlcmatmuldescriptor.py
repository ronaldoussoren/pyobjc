from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCMatMulDescriptor(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCMatMulDescriptor.transposesX)
        self.assertResultIsBOOL(MLCompute.MLCMatMulDescriptor.transposesY)

        self.assertArgIsBOOL(
            MLCompute.MLCMatMulDescriptor.descriptorWithAlpha_transposesX_transposesY_,
            1,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCMatMulDescriptor.descriptorWithAlpha_transposesX_transposesY_,
            2,
        )
