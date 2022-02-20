from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc
import PhotosUI


class TestPHLivePhotoViewHelper(PhotosUI.NSObject):
    def livePhotoView_willBeginPlaybackWithStyle_(self, v, s):
        pass

    def livePhotoView_didEndPlaybackWithStyle_(self, v, s):
        pass

    def livePhotoView_canBeginPlaybackWithStyle_(self, v, s):
        return 1


class TestPHLivePhotoView(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(PhotosUI.PHLivePhotoViewContentMode)
        self.assertIsEnumType(PhotosUI.PHLivePhotoViewPlaybackStyle)

    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(PhotosUI.PHLivePhotoViewPlaybackStyleUndefined, 0)
        self.assertEqual(PhotosUI.PHLivePhotoViewPlaybackStyleFull, 1)
        self.assertEqual(PhotosUI.PHLivePhotoViewPlaybackStyleHint, 2)

        self.assertEqual(PhotosUI.PHLivePhotoViewContentModeAspectFit, 0)
        self.assertEqual(PhotosUI.PHLivePhotoViewContentModeAspectFill, 1)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(PhotosUI.PHLivePhotoView.isMuted)
        self.assertArgIsBOOL(PhotosUI.PHLivePhotoView.setMuted_, 0)
        self.assertArgIsBOOL(PhotosUI.PHLivePhotoView.stopPlaybackAnimated_, 0)

    @min_sdk_level("10.12")
    def testProtocolMethods(self):
        self.assertArgHasType(
            TestPHLivePhotoViewHelper.livePhotoView_willBeginPlaybackWithStyle_,
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestPHLivePhotoViewHelper.livePhotoView_didEndPlaybackWithStyle_,
            1,
            objc._C_NSInteger,
        )

        self.assertResultHasType(
            TestPHLivePhotoViewHelper.livePhotoView_canBeginPlaybackWithStyle_,
            objc._C_NSBOOL,
        )
        self.assertArgHasType(
            TestPHLivePhotoViewHelper.livePhotoView_canBeginPlaybackWithStyle_,
            1,
            objc._C_NSInteger,
        )

    @min_sdk_level("10.12")
    def testProtocols(self):
        self.assertIsInstance(
            objc.protocolNamed("PHLivePhotoViewDelegate"), objc.formal_protocol
        )
