from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSMatrix_MPSMatrixMultiplication(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixMultiplication.initWithDevice_transposeLeft_transposeRight_resultRows_resultColumns_interiorColumns_alpha_beta_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixMultiplication.initWithDevice_transposeLeft_transposeRight_resultRows_resultColumns_interiorColumns_alpha_beta_,  # noqa: B950
            2,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixVectorMultiplication.initWithDevice_transpose_rows_columns_alpha_beta_,
            1,
        )
