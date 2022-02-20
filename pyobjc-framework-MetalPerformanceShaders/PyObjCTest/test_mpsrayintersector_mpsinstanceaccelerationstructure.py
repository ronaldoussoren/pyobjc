from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders

MPSAccelerationStructureCompletionHandler = b"v@"


class TestMPSRayIntersector_MPSInstanceAccelerationStructure(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSTransformType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSTransformTypeFloat4x4, 0)
        self.assertEqual(MetalPerformanceShaders.MPSTransformTypeIdentity, 1)
