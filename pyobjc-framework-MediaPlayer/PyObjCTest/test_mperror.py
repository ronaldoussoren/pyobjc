from PyObjCTools.TestSupport import TestCase, min_os_level
import MediaPlayer


class TestMPError(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertIsInstance(MediaPlayer.MPErrorDomain, str)

        self.assertEqual(MediaPlayer.MPErrorUnknown, 0)
        self.assertEqual(MediaPlayer.MPErrorPermissionDenied, 1)
        self.assertEqual(MediaPlayer.MPErrorCloudServiceCapabilityMissing, 2)
        self.assertEqual(MediaPlayer.MPErrorNetworkConnectionFailed, 3)
        self.assertEqual(MediaPlayer.MPErrorNotFound, 4)
        self.assertEqual(MediaPlayer.MPErrorNotSupported, 5)
        self.assertEqual(MediaPlayer.MPErrorCancelled, 6)
        self.assertEqual(MediaPlayer.MPErrorRequestTimedOut, 7)
