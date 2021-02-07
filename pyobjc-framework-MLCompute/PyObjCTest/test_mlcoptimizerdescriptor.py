from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCOptimizerDescriptor(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            MLCompute.MLCOptimizerDescriptor.appliesGradientClipping
        )
