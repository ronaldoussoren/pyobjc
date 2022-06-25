from PyObjCTools.TestSupport import TestCase
import objc

import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper(
    MetalPerformanceShaders.NSObject
):
    def gamma(self):
        return 1

    def beta(self):
        return 1

    def numberOfFeatureChannels(self):
        return 1

    def updateGammaAndBetaWithInstanceNormalizationStateBatch_(self, a):
        return 1

    def epsilon(self):
        return 1

    def supportsSecureCoding(self):
        return 1

    def copyWithZone_device_(self, a, b):
        return 1

    def load(self):
        return 1


class TestMPSNeuralNetwork_MPSCNNInstanceNormalization(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("MPSCNNInstanceNormalizationDataSource")

    def test_methods(self):
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.gamma, b"^f"
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.gamma
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.beta, b"^f"
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.beta
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.numberOfFeatureChannels,
            objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.updateGammaAndBetaWithInstanceNormalizationStateBatch_
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.numberOfFeatureChannels,
            objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.supportsSecureCoding
        )

        self.assertArgHasType(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.copyWithZone_device_,
            0,
            b"^{_NSZone=}",
        )

        self.assertResultIsBOOL(
            TestMPSNeuralNetwork_MPSCNNInstanceNormalizationHelper.load
        )
