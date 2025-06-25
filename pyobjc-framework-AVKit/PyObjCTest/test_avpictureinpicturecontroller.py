from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import AVKit


class TestAVPictureInPictureControllerHelper(AVKit.NSObject):
    def pictureInPictureController_restoreUserInterfaceForPictureInPictureStopWithCompletionHandler_(  # noqa: B950
        self, a, b
    ):
        pass


class TestAVPictureInPictureController(TestCase):
    @min_sdk_level("10.15")
    def testProtocols(self):
        self.assertProtocolExists("AVPictureInPictureControllerDelegate")

    @min_os_level("10.15")
    def test_methods(self):
        self.assertResultIsBOOL(
            AVKit.AVPictureInPictureController.isPictureInPictureSupported
        )
        self.assertResultIsBOOL(
            AVKit.AVPictureInPictureController.isPictureInPicturePossible
        )
        self.assertResultIsBOOL(
            AVKit.AVPictureInPictureController.isPictureInPictureActive
        )
        self.assertResultIsBOOL(
            AVKit.AVPictureInPictureController.isPictureInPictureSuspended
        )

        self.assertArgIsBlock(
            TestAVPictureInPictureControllerHelper.pictureInPictureController_restoreUserInterfaceForPictureInPictureStopWithCompletionHandler_,  # noqa: B950
            1,
            b"vZ",
        )

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(AVKit.AVPictureInPictureController.requiresLinearPlayback)
        self.assertArgIsBOOL(
            AVKit.AVPictureInPictureController.setRequiresLinearPlayback_, 0
        )

        self.assertResultIsBOOL(
            AVKit.AVPictureInPictureController.canStopPictureInPicture
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertResultIsBOOL(
            AVKit.AVPictureInPictureController.canStartPictureInPictureAutomaticallyFromInline
        )
        self.assertArgIsBOOL(
            AVKit.AVPictureInPictureController.setCanStartPictureInPictureAutomaticallyFromInline_,
            0,
        )
