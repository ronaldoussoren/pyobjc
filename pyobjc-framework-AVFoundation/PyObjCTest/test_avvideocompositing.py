import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestAVVideoCompositingHelper(AVFoundation.NSObject):
    def enablePostProcessing(self):
        return 1

    def containsTweening(self):
        return 1

    def passthroughTrackID(self):
        return 1

    def supportsWideColorSourceFrames(self):
        return 1

    def canConformColorOfSourceFrames(self):
        return 1

    def supportsHDRSourceFrames(self):
        return 1


class TestAVVideoCompositing(TestCase):
    def testStructs(self):
        v = AVFoundation.AVPixelAspectRatio()
        self.assertIsInstance(v.horizontalSpacing, int)
        self.assertIsInstance(v.verticalSpacing, int)
        self.assertPickleRoundTrips(v)

        v = AVFoundation.AVEdgeWidths()
        self.assertIsInstance(v.left, float)
        self.assertIsInstance(v.top, float)
        self.assertIsInstance(v.right, float)
        self.assertIsInstance(v.bottom, float)
        self.assertPickleRoundTrips(v)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(
            AVFoundation.AVVideoCompositionRenderContext.highQualityRendering
        )

    # @expectedFailure  # XXX
    @min_os_level("11.0")
    def testMethods11_0(self):
        self.assertResultIsBOOL(
            AVFoundation.TestAVVideoCompositingHelper.supportsHDRSourceFrames
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(
            AVFoundation.TestAVVideoCompositingHelper.canConformColorOfSourceFrames
        )

    def testProtocolMethods(self):
        self.assertResultIsBOOL(TestAVVideoCompositingHelper.enablePostProcessing)
        self.assertResultIsBOOL(TestAVVideoCompositingHelper.containsTweening)
        self.assertResultHasType(
            TestAVVideoCompositingHelper.passthroughTrackID, objc._C_INT
        )
        self.assertResultIsBOOL(
            TestAVVideoCompositingHelper.supportsWideColorSourceFrames
        )

    @min_sdk_level("10.9")
    def testProtocols(self):
        self.assertProtocolExists("AVVideoCompositing")
        self.assertProtocolExists("AVVideoCompositionInstruction")
