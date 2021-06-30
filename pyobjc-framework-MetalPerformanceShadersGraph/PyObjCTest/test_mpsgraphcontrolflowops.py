from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShadersGraph

# XXX: Blocks appear to be variadic?
MPSGraphControlFlowDependencyBlock = b"@"
MPSGraphIfThenElseBlock = b"@"
MPSGraphWhileBeforeBlock = b"@@@"
MPSGraphWhileAfterBlock = b"@@"
MPSGraphForLoopBodyBlock = b"@@@"


class TestMPSGraphControlFlowOps(TestCase):
    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraph.controlDependencyWithOperations_dependentBlock_name_,
            1,
            MPSGraphControlFlowDependencyBlock,
        )

        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraph.ifWithPredicateTensor_thenBlock_elseBlock_name_,
            1,
            MPSGraphIfThenElseBlock,
        )
        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraph.ifWithPredicateTensor_thenBlock_elseBlock_name_,
            2,
            MPSGraphIfThenElseBlock,
        )

        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraph.whileWithInitialInputs_before_after_name_,
            1,
            MPSGraphWhileBeforeBlock,
        )
        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraph.whileWithInitialInputs_before_after_name_,
            2,
            MPSGraphWhileAfterBlock,
        )

        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraph.forLoopWithLowerBound_upperBound_step_initialBodyArguments_body_name_,
            4,
            MPSGraphForLoopBodyBlock,
        )

        self.assertArgIsBlock(
            MetalPerformanceShadersGraph.MPSGraph.forLoopWithNumberOfIterations_initialBodyArguments_body_name_,
            2,
            MPSGraphForLoopBodyBlock,
        )
