from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCSGDOptimizer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCSGDOptimizer.usesNestrovMomentum)

        self.assertArgIsBOOL(
            MLCompute.MLCSGDOptimizer.optimizerWithDescriptor_momentumScale_usesNestrovMomentum_,
            2,
        )
