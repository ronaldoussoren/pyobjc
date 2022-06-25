from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph


class TestMPSGraphRNNOps(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphLossReductionType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphRNNActivationNone, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphRNNActivationRelu, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphRNNActivationTanh, 2)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphRNNActivationSigmoid, 3)
        self.assertEqual(
            MetalPerformanceShadersGraph.MPSGraphRNNActivationHardSigmoid, 4
        )

    @min_os_level("12.3")
    def test_methods12_3(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphSingleGateRNNDescriptor.reverse
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphSingleGateRNNDescriptor.setReverse_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphSingleGateRNNDescriptor.bidirectional
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphSingleGateRNNDescriptor.setBidirectional_,
            0,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphSingleGateRNNDescriptor.training
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphSingleGateRNNDescriptor.setTraining_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.reverse
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.setReverse_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.bidirectional
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.setBidirectional_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.produceCell
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.setProduceCell_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.training
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.setTraining_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.forgetGateLast
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphLSTMDescriptor.setForgetGateLast_, 0
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.reverse
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.setReverse_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.bidirectional
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.setBidirectional_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.training
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.setTraining_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.resetAfter
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.setResetAfter_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.resetGateFirst
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.setResetGateFirst_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.flipZ
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.setFlipZ_, 0
        )

        self.assertResultIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.resetGateFirst
        )
        self.assertArgIsBOOL(
            MetalPerformanceShadersGraph.MPSGraphGRUDescriptor.setResetGateFirst_, 0
        )
