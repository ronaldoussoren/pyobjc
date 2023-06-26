from PyObjCTools.TestSupport import TestCase

import MediaExtension
import objc


class TestMEVideoDecoderExtensionHelper(MediaExtension.NSObject):
    def videoDecoderWithCodecType_videoFormatDescription_videoDecoderSpecifications_extensionDecoderPixelBufferManager_error_(
        self, a, b, c, d, e
    ):
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
        return 1

    def canAcceptFormatDescription_(self, a):
        return 1


class TestMEVideoDecoderExtension(TestCase):
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
        self.assertArgHasType(
            TestMEVideoDecoderExtensionHelper.videoDecoderWithCodecType_videoFormatDescription_videoDecoderSpecifications_extensionDecoderPixelBufferManager_error_,
            0,
            b"Q",
        )
        self.assertArgHasType(
            TestMEVideoDecoderExtensionHelper.videoDecoderWithCodecType_videoFormatDescription_videoDecoderSpecifications_extensionDecoderPixelBufferManager_error_,
            0,
            b"o^@",
        )

        self.assertResultIsBOOL(
            TestMEVideoDecoderExtensionHelper.contentHasInterframeDependencies
        )

        self.assertResultHasType(
            TestMEVideoDecoderExtensionHelper.recommendedThreadCount, objc._C_NSInteger
        )
        self.assertArgHasType(
            TestMEVideoDecoderExtensionHelper.setRecommendedThreadCount_,
            0,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestMEVideoDecoderExtensionHelper.actualThreadCount, objc._C_NSInteger
        )

        self.assertResultHasType(
            TestMEVideoDecoderExtensionHelper.reducedResolution,
            MediaExtension.CGSize.__typestr__,
        )
        self.assertArgHasType(
            TestMEVideoDecoderExtensionHelper.setReducedResolution_,
            0,
            MediaExtension.CGSize.__typestr__,
        )

        self.assertResultIsBOOL(
            TestMEVideoDecoderExtensionHelper.isReadyForMoreMediaData
        )

        self.assertArgIsBlock(
            TestMEVideoDecoderExtensionHelper.decodeFrameFromSampleBuffer_options_completionHandler_,
            2,
            b"v@Q@",
        )

        self.assertResultIsBOOL(
            TestMEVideoDecoderExtensionHelper.canAcceptFormatDescription_
        )

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
