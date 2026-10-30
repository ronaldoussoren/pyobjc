from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShaders

MPSAccelerationStructureCompletionHandler = b"v@"


class TestMPSRayIntersector_MPSPolygonAccelerationStructure(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSPolygonType)
        self.assertEqual(MetalPerformanceShaders.MPSPolygonTypeTriangle, 0)
        self.assertEqual(MetalPerformanceShaders.MPSPolygonTypeQuadrilateral, 1)
