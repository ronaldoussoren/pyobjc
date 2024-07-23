from PyObjCTools.TestSupport import TestCase

import MediaExtension


class TestMEVideoDecoderHelper(MediaExtension.NSObject):
    def videoDecoderWithCodecType_videoFormatDescription_videoDecoderSpecifications_extensionDecoderPixelBufferManager_error_(
        self, a, b, c, d, e
    ):
        pass

    def producesRAWOutput(self):
        return 1

    def contentHasInterframeDependencies(self):
        return 1

    def recommendedThreadCount(self):
        return 1

    def setRecommendedThreadCount_(self, a):
        pass

    def actualThreadCount(self):
        return 1

    def reducedResolution(self):
        return 1

    def setReducedResolution_(self, a):
        pass

    def isReadyForMoreMediaData(self):
        return 1

    def decodeFrameFromSampleBuffer_options_completionHandler_(self, a, b, c):
        pass

    def canAcceptFormatDescription_(self, a):
        pass


class TestMEVideoDecoder(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            MediaExtension.MEVideoDecoderReadyForMoreMediaDataDidChangeNotification, str
        )

        self.assertIsEnumType(MediaExtension.MEDecodeFrameStatus)
        self.assertEqual(MediaExtension.MEDecodeFrameNoStatus, 0)
        self.assertEqual(MediaExtension.MEDecodeFrameFrameDropped, 1 << 0)

    def test_protocols(self):
        self.assertProtocolExists("MEVideoDecoderExtension")
        self.assertProtocolExists("MEVideoDecoder")

    def test_protocol_methods(self):
        self.assertArgIsOut(
            TestMEVideoDecoderHelper.videoDecoderWithCodecType_videoFormatDescription_videoDecoderSpecifications_extensionDecoderPixelBufferManager_error_,
            4,
        )

        self.assertResultIsBOOL(TestMEVideoDecoderHelper.producesRAWOutput)
        self.assertResultIsBOOL(
            TestMEVideoDecoderHelper.contentHasInterframeDependencies
        )
        self.assertResultHasType(TestMEVideoDecoderHelper.recommendedThreadCount, b"q")
        self.assertArgHasType(
            TestMEVideoDecoderHelper.setRecommendedThreadCount_, 0, b"q"
        )
        self.assertResultHasType(TestMEVideoDecoderHelper.actualThreadCount, b"q")
        self.assertResultHasType(
            TestMEVideoDecoderHelper.reducedResolution,
            MediaExtension.CGSize.__typestr__,
        )
        self.assertResultIsBOOL(TestMEVideoDecoderHelper.isReadyForMoreMediaData)
        self.assertArgIsBlock(
            TestMEVideoDecoderHelper.decodeFrameFromSampleBuffer_options_completionHandler_,
            2,
            b"v^{__CVBuffer=}Q@",
        )
        self.assertResultIsBOOL(TestMEVideoDecoderHelper.canAcceptFormatDescription_)

    def test_methods(self):
        self.assertArgIsOut(
            MediaExtension.MEVideoDecoderPixelBufferManager.createPixelBufferAndReturnError_,
            0,
        )

        self.assertResultIsBOOL(MediaExtension.MEDecodeFrameOptions.doNotOutputFrame)
        self.assertArgIsBOOL(
            MediaExtension.MEDecodeFrameOptions.setDoNotOutputFrame_, 0
        )

        self.assertResultIsBOOL(MediaExtension.MEDecodeFrameOptions.realTimePlayback)
        self.assertArgIsBOOL(
            MediaExtension.MEDecodeFrameOptions.setRealTimePlayback_, 0
        )
