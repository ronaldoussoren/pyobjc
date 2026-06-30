from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphCore(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphDeviceType)
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphDeviceTypeMetal, 0)
