from PyObjCTools.TestSupport import TestCase
import objc
import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper(
    MetalPerformanceShaders.NSObject
):
    def numberOfFeatureChannels(self):
        return 1

    def gamma(self):
        return 1

    def beta(self):
        return 1

    def mean(self):
        return 1

    def variance(self):
        return 1

    def load(self):
        return 1

    def purge(self):
        return 1

    def label(self):
        return 1

    def updateGammaAndBetaWithBatchNormalizationState_(self, a):
        return 1

    def updateMeanAndVarianceWithBatchNormalizationState_(self, a):
        return 1

    def epsilon(self):
        return 1

    def supportsSecureCoding(self):
        return 1

    def copyWithZone_device_(self, a, b):
        return 1


class TestMPSNeuralNetwork_MPSNNBatchNormalization(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MPSCNNBatchNormalizationDataSource")

    def test_methods(self):
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.numberOfFeatureChannels,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.gamma,
            objc._C_PTR + objc._C_FLT,
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.gamma
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.beta,
            objc._C_PTR + objc._C_FLT,
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.beta
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.mean,
            objc._C_PTR + objc._C_FLT,
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.mean
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.variance,
            objc._C_PTR + objc._C_FLT,
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.variance
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.load, objc._C_NSBOOL
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.updateGammaAndBetaWithBatchNormalizationState_,
            objc._C_NSBOOL,
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.updateMeanAndVarianceWithBatchNormalizationState_,
            objc._C_NSBOOL,
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.epsilon, objc._C_FLT
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.supportsSecureCoding,
            objc._C_NSBOOL,
        )

        self.assertArgHasType(
            TestMPSNeuralNetwork_MPSNNBatchNormalizationHelper.copyWithZone_device_,
            0,
            b"^{_NSZone=}",
        )
