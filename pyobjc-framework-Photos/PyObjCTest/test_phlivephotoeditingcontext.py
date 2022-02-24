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
    def test_typed_enum(self):
        self.assertIsTypedEnum(Photos.PHLivePhotoEditingOption, str)

    def test_enum_types(self):
        self.assertIsEnumType(Photos.PHLivePhotoEditingErrorCode)
        self.assertIsEnumType(Photos.PHLivePhotoFrameType)

    @min_os_level("10.12")
    def testMethods(self):
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
            TestPHLivePhotoEditingContextHelper.time, b"{_CMTime=qiIq}"
        )  # Photos.CMTime.__typestr__
        self.assertResultHasType(
            TestPHLivePhotoEditingContextHelper.type, objc._C_NSInteger
        )
        self.assertResultHasType(
            TestPHLivePhotoEditingContextHelper.renderScale, objc._C_CGFloat
        )

    @min_os_level("10.12")
    def testContants(self):
        self.assertEqual(Photos.PHLivePhotoFrameTypePhoto, 0)
        self.assertEqual(Photos.PHLivePhotoFrameTypeVideo, 1)

        self.assertIsInstance(Photos.PHLivePhotoEditingErrorDomain, str)
        self.assertIsInstance(Photos.PHLivePhotoShouldRenderAtPlaybackTime, str)

        self.assertEqual(Photos.PHLivePhotoEditingErrorCodeUnknown, 0)
        self.assertEqual(Photos.PHLivePhotoEditingErrorCodeAborted, 1)

    @min_sdk_level("10.12")
    def testProtocols(self):
        objc.protocolNamed("PHLivePhotoFrame")
