from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders

MPSAccelerationStructureCompletionHandler = b"v@"


class TestMPSRayIntersector_MPSPolygonAccelerationStructure(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSPolygonType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSPolygonTypeTriangle, 0)
        self.assertEqual(MetalPerformanceShaders.MPSPolygonTypeQuadrilateral, 1)
