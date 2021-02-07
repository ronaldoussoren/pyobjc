from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCSGDOptimizer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCSGDOptimizer.usesNesterovMomentum)

        self.assertArgIsBOOL(
            MLCompute.MLCSGDOptimizer.optimizerWithDescriptor_momentumScale_usesNesterovMomentum_,
            2,
        )
