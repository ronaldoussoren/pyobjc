from PyObjCTools.TestSupport import TestCase, min_os_level

import MLCompute


class TestMLCOptimizer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCOptimizer.appliesGradientClipping)

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBOOL(
            MLCompute.MLCOptimizerDescriptor.descriptorWithLearningRate_gradientRescale_appliesGradientClipping_gradientClippingType_gradientClipMax_gradientClipMin_maximumClippingNorm_customGlobalNorm_regularizationType_regularizationScale_,  # noqa: B950
            2,
        )
