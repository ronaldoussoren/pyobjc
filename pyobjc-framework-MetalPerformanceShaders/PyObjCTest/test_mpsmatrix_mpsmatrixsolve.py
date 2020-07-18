from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSMatrixMPSMatrixSolve(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixSolveTriangular.initWithDevice_right_upper_transpose_unit_order_numberOfRightHandSides_alpha_,  # noqa: B950
            1,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixSolveTriangular.initWithDevice_right_upper_transpose_unit_order_numberOfRightHandSides_alpha_,  # noqa: B950
            2,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixSolveTriangular.initWithDevice_right_upper_transpose_unit_order_numberOfRightHandSides_alpha_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixSolveTriangular.initWithDevice_right_upper_transpose_unit_order_numberOfRightHandSides_alpha_,  # noqa: B950
            4,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixSolveLU.initWithDevice_transpose_order_numberOfRightHandSides_,
            1,
        )

        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixSolveCholesky.initWithDevice_upper_order_numberOfRightHandSides_,
            1,
        )
