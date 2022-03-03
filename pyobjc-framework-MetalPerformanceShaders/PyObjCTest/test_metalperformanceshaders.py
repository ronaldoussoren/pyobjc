from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMetalPerformanceShaders(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSImageEdgeMode)
        self.assertIsEnumType(MetalPerformanceShaders.MPSKernelOptions)

    def test_constants(self):
        self.assertEqual(MetalPerformanceShaders.MPSDeviceOptionsDefault, 0)
        self.assertEqual(MetalPerformanceShaders.MPSDeviceOptionsLowPower, 1)
        self.assertEqual(MetalPerformanceShaders.MPSDeviceOptionsSkipRemovable, 2)

    @min_os_level("10.13")
    def test_functions10_13(self):
        self.assertResultIsBOOL(MetalPerformanceShaders.MPSSupportsMTLDevice)

    @min_os_level("10.14")
    def test_functions10_14(self):
        MetalPerformanceShaders.MPSSetHeapCacheDuration
        MetalPerformanceShaders.MPSHintTemporaryMemoryHighWaterMark
        MetalPerformanceShaders.MPSGetPreferredDevice
