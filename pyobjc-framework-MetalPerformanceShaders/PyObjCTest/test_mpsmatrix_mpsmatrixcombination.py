from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSMatrix_MPSMatrixCombination(TestCase):
    def test_structs(self):
        v = MetalPerformanceShaders.MPSMatrixCopyOffsets()
        self.assertIsInstance(v.sourceRowOffset, int)
        self.assertIsInstance(v.sourceColumnOffset, int)
        self.assertIsInstance(v.destinationRowOffset, int)
        self.assertIsInstance(v.destinationColumnOffset, int)
        self.assertPickleRoundTrips(v)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixCopy.initWithDevice_copyRows_copyColumns_sourcesAreTransposed_destinationsAreTransposed_,  # noqa: B950
            3,
        )
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSMatrixCopy.initWithDevice_copyRows_copyColumns_sourcesAreTransposed_destinationsAreTransposed_,  # noqa: B950
            4,
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSMatrixCopy.sourcesAreTransposed
        )
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSMatrixCopy.destinationsAreTransposed
        )
