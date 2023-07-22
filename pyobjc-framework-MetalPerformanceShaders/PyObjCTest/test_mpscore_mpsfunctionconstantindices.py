from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSCore_MPSFunctionConstantIndices(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSDeviceCapsIndex, 127)
        self.assertEqual(
            MetalPerformanceShaders.MPSFunctionConstantIndex,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 1,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSBatchSizeIndex,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 2,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSUserConstantIndex,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 3,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNDArrayConstantIndex,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 4,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSFunctionConstantIndexReserved,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 5,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSTextureLinkingConstantIndex,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 6,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNDArrayConstantMultiDestIndex,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 7,
        )

        self.assertEqual(
            MetalPerformanceShaders.MPSNDArrayConstantMultiDestIndex0,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 8,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNDArrayConstantMultiDestIndex1,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 9,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNDArrayConstantMultiDestSrcAddressingIndex,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 10,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSNDArrayConstantMultiDestDstAddressingIndex,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 11,
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSUserAvailableFunctionConstantStartIndex,
            MetalPerformanceShaders.MPSDeviceCapsIndex - 12,
        )
