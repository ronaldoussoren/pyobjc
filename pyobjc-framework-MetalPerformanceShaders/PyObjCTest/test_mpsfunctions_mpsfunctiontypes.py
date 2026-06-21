from PyObjCTools.TestSupport import TestCase
import MetalPerformanceShaders


class TestMPSFunctions_MPSFunctionTypes(TestCase):
    def test_structs(self):
        v = MetalPerformanceShaders.MPSFunctions_AABB()
        self.assertEqual(v.max, None)
        self.assertEqual(v.min, None)
