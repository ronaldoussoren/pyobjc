import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayerOutputHelper(AVFoundation.NSObject):
    def legibleOutput_didOutputAttributedStrings_nativeSampleBuffers_forItemTime_(  # noqa: B950
        self, a, b, c, d
    ):
        pass

    def renderedLegibleOutput_didOutputRenderedCaptionImages_forItemTime_(self, a, b, c):
        pass


class TestAVPlayerOutput(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(
            AVFoundation.AVPlayerItemLegibleOutputTextStylingResolution, str
        )

    @min_os_level("10.9")
    def testConstants10_9(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerItemLegibleOutputTextStylingResolutionDefault,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly,  # noqa: B950
            str,
        )

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertResultIsBOOL(AVFoundation.AVPlayerItemOutput.suppressesPlayerRendering)
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItemOutput.setSuppressesPlayerRendering_, 0
        )

        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItemVideoOutput.hasNewPixelBufferForItemTime_
        )

        self.assertResultIsCFRetained(
            AVFoundation.AVPlayerItemVideoOutput.copyPixelBufferForItemTime_itemTimeForDisplay_  # noqa: B950
        )
        self.assertArgIsOut(
            AVFoundation.AVPlayerItemVideoOutput.copyPixelBufferForItemTime_itemTimeForDisplay_,  # noqa: B950
            1,
        )

    def testProtocols(self):
        self.assertProtocolExists("AVPlayerItemOutputPullDelegate")
        self.assertProtocolExists("AVPlayerItemLegibleOutputPushDelegate")
        self.assertProtocolExists("AVPlayerItemMetadataOutputPushDelegate")
        self.assertProtocolExists("AVPlayerItemOutputPushDelegate")
        self.assertProtocolExists("AVPlayerItemRenderedLegibleOutputPushDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestAVPlayerOutputHelper.legibleOutput_didOutputAttributedStrings_nativeSampleBuffers_forItemTime_,  # noqa: B950
            3,
            b"{CMTime=qiIq}",
        )

        self.assertArgHasType(
            TestAVPlayerOutputHelper.renderedLegibleOutput_didOutputRenderedCaptionImages_forItemTime_,  # noqa: B950
            2,
            b"{CMTime=qiIq}",
        )
