from PyObjCTools.TestSupport import TestCase

import MetalPerformanceShadersGraph


class TestMPSGraphCore(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShadersGraph.MPSGraphDeviceType)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShadersGraph.MPSGraphDeviceTypeMetal, 0)
