from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCOptimizer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCOptimizer.appliesGradientClipping)
