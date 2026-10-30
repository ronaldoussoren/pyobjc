from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc
import Photos


class TestPHLivePhotoEditingContextHelper(Photos.NSObject):
    def time(self):
        return 1

    def type(self):  # noqa: A003
        return 1

    def renderScale(self):
        return 1


class TestPHLivePhotoEditingContext(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Photos.PHLivePhotoEditingErrorCode)
        self.assertEqual(Photos.PHLivePhotoEditingErrorCodeUnknown, 0)
        self.assertEqual(Photos.PHLivePhotoEditingErrorCodeAborted, 1)

        self.assertIsEnumType(Photos.PHLivePhotoFrameType)
        self.assertEqual(Photos.PHLivePhotoFrameTypePhoto, 0)
        self.assertEqual(Photos.PHLivePhotoFrameTypeVideo, 1)

    def test_typed_enums(self):
        self.assertIsTypedEnum(Photos.PHLivePhotoEditingOption, str)

    @min_os_level("10.12")
    def test_constants(self):
        self.assertIsInstance(Photos.PHLivePhotoEditingErrorDomain, str)
        self.assertIsInstance(Photos.PHLivePhotoShouldRenderAtPlaybackTime, str)

    @min_os_level("10.12")
    def test_methods(self):
        PHLivePhotoFrameProcessingBlock = b"@@o^@"

        self.assertResultIsBlock(
            Photos.PHLivePhotoEditingContext.frameProcessor,
            PHLivePhotoFrameProcessingBlock,
        )
        self.assertArgIsBlock(
            Photos.PHLivePhotoEditingContext.setFrameProcessor_,
            0,
            PHLivePhotoFrameProcessingBlock,
        )

        self.assertArgIsBlock(
            Photos.PHLivePhotoEditingContext.prepareLivePhotoForPlaybackWithTargetSize_options_completionHandler_,
            2,
            b"vZ@",
        )
        self.assertArgIsBlock(
            Photos.PHLivePhotoEditingContext.saveLivePhotoToOutput_options_completionHandler_,
            2,
            b"vZ@",
        )

        self.assertResultHasType(
            Photos.PHLivePhotoEditingContext.duration, b"{CMTime=qiIq}"
        )
        self.assertResultHasType(
            Photos.PHLivePhotoEditingContext.photoTime, b"{CMTime=qiIq}"
        )

    @min_sdk_level("10.12")
    def test_protocols(self):
        self.assertProtocolExists("PHLivePhotoFrame", Photos)

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestPHLivePhotoEditingContextHelper.time, b"{CMTime=qiIq}"
        )
        self.assertResultHasType(
            TestPHLivePhotoEditingContextHelper.type, objc._C_NSInteger
        )
        self.assertResultHasType(
            TestPHLivePhotoEditingContextHelper.renderScale, objc._C_CGFloat
        )
