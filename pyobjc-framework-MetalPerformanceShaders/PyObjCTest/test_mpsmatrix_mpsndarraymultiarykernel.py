from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSMatrix_MPSNDArrayMultiaryKernel(TestCase):
    @min_os_level("10.15")
    def test_methods10_15(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNDArrayMultiaryKernel.encodeToCommandBuffer_sourceArrays_resultState_outputStateIsTemporary_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNDArrayUnaryKernel.encodeToCommandBuffer_sourceArray_resultState_outputStateIsTemporary_,
            3,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSNDArrayBinaryKernel.encodeToCommandBuffer_primarySourceArray_secondarySourceArray_resultState_outputStateIsTemporary_,  # noqa: B950
            4,
        )
