from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCRMSPropOptimizer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.TestMLCRMSPropOptimizer.isCentered)

        self.assertArgIsBOOL(
            MLCompute.TestMLCRMSPropOptimizer.optimizerWithDescriptor_momentumScale_alpha_epsilon_isCentered_,
            4,
        )
