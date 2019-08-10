import sys
from PyObjCTools.TestSupport import *


if sys.maxsize > 2 ** 32:
    import AVKit

    class TestAVPictureInPictureControllerHelper(AVKit.NSObject):
        def pictureInPictureController_restoreUserInterfaceForPictureInPictureStopWithCompletionHandler_(
            self, a, b
        ):
            pass

    class TestAVPictureInPictureController(TestCase):
        @min_sdk_level("10.15")
        def testProtocols(self):
            objc.protocolNamed("AVPictureInPictureControllerDelegate")

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
                TestAVPictureInPictureControllerHelper.pictureInPictureController_restoreUserInterfaceForPictureInPictureStopWithCompletionHandler_,
                1,
                b"vZ",
            )


if __name__ == "__main__":
    main()
