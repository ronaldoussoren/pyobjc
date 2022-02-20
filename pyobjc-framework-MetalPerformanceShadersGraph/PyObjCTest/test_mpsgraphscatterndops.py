from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphScatterNDOps(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphScatterMode)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphScatterModeAdd, 0)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphScatterModeSub, 1)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphScatterModeMul, 2)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphScatterModeDiv, 3)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphScatterModeMin, 4)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphScatterModeMax, 5)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphScatterModeSet, 6)
