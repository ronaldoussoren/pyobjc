from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders


class TestMPSNDArray_MPSNDArrayTypes(TestCase):
    def test_structs(self):
        v = MetalPerformanceShaders.MPSNDArrayOffsets()
        self.assertEqual(v.dimensions, None)  # [0] * 16)
        self.assertPickleRoundTrips(v)

        v = MetalPerformanceShaders.MPSNDArraySizes()
        self.assertEqual(v.dimensions, None)  # [0] * 16)
        self.assertPickleRoundTrips(v)
