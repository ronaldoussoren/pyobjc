from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCRMSPropOptimizer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCRMSPropOptimizer.isCentered)

        self.assertArgIsBOOL(
            MLCompute.MLCRMSPropOptimizer.optimizerWithDescriptor_momentumScale_alpha_epsilon_isCentered_,
            4,
        )
