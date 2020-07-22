from PyObjCTools.TestSupport import TestCase
import objc
import MetalPerformanceShaders


class TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper(
    MetalPerformanceShaders.NSObject
):
    def gamma(self):
        return 1

    def beta(self):
        return 1

    def numberOfFeatureChannels(self):
        return 1

    def numberOfGroups(self):
        return 1

    def updateGammaAndBetaWithGroupNormalizationStateBatch_(self, a):
        return 1

    def epsilon(self):
        return 1

    def supportsSecureCoding(self):
        return 1

    def copyWithZone_(self, zone):
        return 1


class TestMPSNeuralNetwork_MPSCNNGroupNormalization(TestCase):
    def test_protocols(self):
        objc.protocolNamed("MPSCNNGroupNormalizationDataSource")

    def test_methods(self):
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.beta, b"^f"
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.beta
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.gamma, b"^f"
        )
        self.assertResultIsVariableSize(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.gamma
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.numberOfFeatureChannels,
            objc._C_NSUInteger,
        )
        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.numberOfGroups,
            objc._C_NSUInteger,
        )

        self.assertResultIsBOOL(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.updateGammaAndBetaWithGroupNormalizationStateBatch_
        )

        self.assertResultHasType(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.epsilon, b"f"
        )

        self.assertResultIsBOOL(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.supportsSecureCoding
        )

        self.assertArgHasType(
            TestMPSNeuralNetwork_MPSCNNGroupNormalizationHelper.copyWithZone_,
            0,
            b"^{_NSZone=}",
        )
