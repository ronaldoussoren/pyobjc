from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMetalPerformanceShaders(TestCase):
    def test_enums(self):
        self.assertIsEnumType(MetalPerformanceShaders.MPSImageEdgeMode)
        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeZero, 0)
        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeClamp, 1)
        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeMirror, 2)
        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeMirrorWithEdge, 3)
        self.assertEqual(MetalPerformanceShaders.MPSImageEdgeModeConstant, 4)

        self.assertIsEnumType(MetalPerformanceShaders.MPSKernelOptions)
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


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(MetalPerformanceShaders)
