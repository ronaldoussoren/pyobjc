from PyObjCTools.TestSupport import TestCase, min_os_level
import MediaPlayer
import objc


class TestMPRemoteCommand(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(MediaPlayer.MPRemoteCommandHandlerStatusSuccess, 0)
        self.assertEqual(MediaPlayer.MPRemoteCommandHandlerStatusNoSuchContent, 100)
        self.assertEqual(
            MediaPlayer.MPRemoteCommandHandlerStatusNoActionableNowPlayingItem, 110
        )
        self.assertEqual(MediaPlayer.MPRemoteCommandHandlerStatusDeviceNotFound, 120)
        self.assertEqual(MediaPlayer.MPRemoteCommandHandlerStatusCommandFailed, 200)

    @min_os_level("10.12")
    def testMethods(self):
        self.assertResultIsBOOL(MediaPlayer.MPRemoteCommand.isEnabled)
        self.assertArgIsBOOL(MediaPlayer.MPRemoteCommand.setEnabled_, 0)

        self.assertArgIsBlock(
            MediaPlayer.MPRemoteCommand.addTargetWithHandler_,
            0,
            objc._C_NSInteger + b"@",
        )

        self.assertResultIsBOOL(MediaPlayer.MPFeedbackCommand.isActive)
        self.assertArgIsBOOL(MediaPlayer.MPFeedbackCommand.setActive_, 0)
