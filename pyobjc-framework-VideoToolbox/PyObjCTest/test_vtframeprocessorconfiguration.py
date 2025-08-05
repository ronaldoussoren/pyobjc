import VideoToolbox
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestVTFrameProcessorConfigurationHelper(VideoToolbox.NSObject):
    def processorSupported(self):
        return 1

    def nextFrameCount(self):
        return 1

    def previousFrameCount(self):
        return 1

    def maximumDimensions(self):
        return 1

    def minimumDimensions(self):
        return 1

    def isSupported(self):
        return 1


class TestVTFrameProcessorConfiguration(TestCase):
    @min_sdk_level("15.4")
    def test_protocols(self):
        self.assertProtocolExists("VTFrameProcessorConfiguration")

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestVTFrameProcessorConfigurationHelper.isSupported)
        self.assertResultHasType(
            TestVTFrameProcessorConfigurationHelper.nextFrameCount, objc._C_NSInteger
        )
        self.assertResultHasType(
            TestVTFrameProcessorConfigurationHelper.previousFrameCount,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestVTFrameProcessorConfigurationHelper.maximumDimensions,
            VideoToolbox.CMVideoDimensions.__typestr__,
        )
        self.assertResultHasType(
            TestVTFrameProcessorConfigurationHelper.minimumDimensions,
            VideoToolbox.CMVideoDimensions.__typestr__,
        )
