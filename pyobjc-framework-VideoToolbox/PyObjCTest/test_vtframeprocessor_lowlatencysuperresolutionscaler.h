import VideoToolbox from PyObjCTools.TestSupport import TestCase, min_os_level

    class TestVTFrameProcessor_LowLatencySuperResolutionScaler(TestCase) : @min_os_level("26.0") def test_methods(self) :self.assertResultIsBOOL(VideoToolbox.VTLowLatencySuperResolutionScalerConfiguration.isSupported)
