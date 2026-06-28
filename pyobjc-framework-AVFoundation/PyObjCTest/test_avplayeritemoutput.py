import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVPlayerOutputHelper(AVFoundation.NSObject):
    def legibleOutput_didOutputAttributedStrings_nativeSampleBuffers_forItemTime_(  # noqa: B950
        self, a, b, c, d
    ):
        pass

    def renderedLegibleOutput_didOutputRenderedCaptionImages_forItemTime_(
        self, a, b, c
    ):
        pass


class TestAVPlayerOutput(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(
            AVFoundation.AVPlayerItemLegibleOutputTextStylingResolution, str
        )

    def test_constants(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerItemLegibleOutputTextStylingResolutionDefault,
            str,  # noqa: B950
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerItemLegibleOutputTextStylingResolutionSourceAndRulesOnly,  # noqa: B950
            str,
        )

    def test_methods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItemOutput.suppressesPlayerRendering
        )
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

    def test_protocols(self):
        self.assertProtocolExists("AVPlayerItemOutputPullDelegate", AVFoundation)
        self.assertProtocolExists("AVPlayerItemLegibleOutputPushDelegate", AVFoundation)
        self.assertProtocolExists(
            "AVPlayerItemMetadataOutputPushDelegate", AVFoundation
        )
        self.assertProtocolExists("AVPlayerItemOutputPushDelegate", AVFoundation)
        self.assertProtocolExists(
            "AVPlayerItemRenderedLegibleOutputPushDelegate", AVFoundation
        )

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
