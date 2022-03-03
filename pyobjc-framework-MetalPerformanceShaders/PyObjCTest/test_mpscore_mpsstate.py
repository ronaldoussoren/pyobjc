from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSCore_MPSState(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSStateResourceType)

    def test_structs(self):
        v = MetalPerformanceShaders.MPSStateTextureInfo()
        self.assertIsInstance(v.width, int)
        self.assertIsInstance(v.height, int)
        self.assertIsInstance(v.depth, int)
        self.assertIsInstance(v.arrayLength, int)
        self.assertIsInstance(v.pixelFormat, int)
        self.assertIsInstance(v.textureType, int)
        self.assertIsInstance(v.usage, int)
        self.assertPickleRoundTrips(v)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSStateResourceTypeNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSStateResourceTypeBuffer, 1)
        self.assertEqual(MetalPerformanceShaders.MPSStateResourceTypeTexture, 2)

    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgIsBOOL(
            MetalPerformanceShaders.MPSState.resourceAtIndex_allocateMemory_, 1
        )
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSState.isTemporary)

    @min_os_level("10.13.4")
    def test_functions(self):
        MetalPerformanceShaders.MPSStateBatchIncrementReadCount
        MetalPerformanceShaders.MPSStateBatchSynchronize

    @min_os_level("10.14")
    def test_functions10_14(self):
        MetalPerformanceShaders.MPSStateBatchResourceSize
