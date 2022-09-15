import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureDeskViewApplication(TestCase):
    @min_os_level("13.0")
    def test_methods(self):
        self.assertArgIsBlock(
            AVFoundation.AVCaptureDeskViewApplication.presentWithCompletionHandler_,
            0,
            b"v@",
        )

        self.assertArgIsBlock(
            AVFoundation.AVCaptureDeskViewApplication.presentWithLaunchConfiguration_completionHandler_,
            1,
            b"v@",
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureDeskViewApplicationLaunchConfiguration.requiresSetUpModeCompletion
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureDeskViewApplicationLaunchConfiguration.setRequiresSetUpModeCompletion_,
            0,
        )
