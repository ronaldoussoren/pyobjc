from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders

MPSAccelerationStructureCompletionHandler = b"v@"


class TestMPSRayIntersector_MPSAccelerationStructure(TestCase):
    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSAccelerationStructureUsageNone, 0)
        self.assertEqual(MetalPerformanceShaders.MPSAccelerationStructureUsageRefit, 1)
        self.assertEqual(
            MetalPerformanceShaders.MPSAccelerationStructureUsageFrequentRebuild, 2
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSAccelerationStructureUsagePreferGPUBuild, 4
        )
        self.assertEqual(
            MetalPerformanceShaders.MPSAccelerationStructureUsagePreferCPUBuild, 8
        )

        self.assertEqual(
            MetalPerformanceShaders.MPSAccelerationStructureStatusUnbuilt, 0
        )
        self.assertEqual(MetalPerformanceShaders.MPSAccelerationStructureStatusBuilt, 1)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertArgIsBlock(
            MetalPerformanceShaders.MPSAccelerationStructure.rebuildWithCompletionHandler_,
            0,
            MPSAccelerationStructureCompletionHandler,
        )
