import AVFoundation
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestAVVideoCompositingHelper(AVFoundation.NSObject):
    def enablePostProcessing(self):
        return 1

    def containsTweening(self):
        return 1

    def passthroughTrackID(self):
        return 1

    def supportsWideColorSourceFrames(self):
        return 1


class TestAVVideoCompositing(TestCase):
    def testStructs(self):
        v = AVFoundation.AVPixelAspectRatio()
        self.assertIsInstance(v.horizontalSpacing, int)
        self.assertIsInstance(v.verticalSpacing, int)

        v = AVFoundation.AVEdgeWidths()
        self.assertIsInstance(v.left, float)
        self.assertIsInstance(v.top, float)
        self.assertIsInstance(v.right, float)
        self.assertIsInstance(v.bottom, float)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertResultIsBOOL(
            AVFoundation.AVVideoCompositionRenderContext.highQualityRendering
        )

    @expectedFailure  # XXX
    @min_os_level("10.16")
    def testMethods10_16(self):
        self.assertResultIsBOOL(
            AVFoundation.AVVideoCompositionRenderContext.supportsHDRSourceFrames
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

    @min_os_level("10.9")
    def testProtocols(self):
        objc.protocolNamed("AVVideoCompositing")
        objc.protocolNamed("AVVideoCompositionInstruction")
