from PyObjCTools.TestSupport import TestCase

import ScreenTime


class TestSTWebpageController(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(ScreenTime.STWebpageController.suppressUsageRecording)
        self.assertArgIsBOOL(
            ScreenTime.STWebpageController.setSuppressUsageRecording_, 0
        )

        self.assertResultIsBOOL(ScreenTime.STWebpageController.URLIsPlayingVideo)
        self.assertArgIsBOOL(ScreenTime.STWebpageController.setURLIsPlayingVideo_, 0)

        self.assertResultIsBOOL(ScreenTime.STWebpageController.URLIsPictureInPicture)
        self.assertArgIsBOOL(
            ScreenTime.STWebpageController.setURLIsPictureInPicture_, 0
        )

        self.assertResultIsBOOL(ScreenTime.STWebpageController.URLIsBlocked)

        self.assertResultIsBOOL(
            ScreenTime.STWebpageController.setBundleIdentifier_error_
        )
        self.assertArgIsOut(
            ScreenTime.STWebpageController.setBundleIdentifier_error_, 1
        )
