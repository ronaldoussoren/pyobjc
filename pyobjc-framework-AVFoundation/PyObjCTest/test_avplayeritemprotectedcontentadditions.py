import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayerItemProtectedContentAdditions(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVContentAuthorizationStatus)

    @min_os_level("10.7")
    def testConstants(self):
        self.assertEqual(AVFoundation.AVContentAuthorizationUnknown, 0)
        self.assertEqual(AVFoundation.AVContentAuthorizationCompleted, 1)
        self.assertEqual(AVFoundation.AVContentAuthorizationCancelled, 2)
        self.assertEqual(AVFoundation.AVContentAuthorizationTimedOut, 3)
        self.assertEqual(AVFoundation.AVContentAuthorizationBusy, 4)
        self.assertEqual(AVFoundation.AVContentAuthorizationNotAvailable, 5)
        self.assertEqual(AVFoundation.AVContentAuthorizationNotPossible, 6)

    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItem.isAuthorizationRequiredForPlayback
        )
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItem.isApplicationAuthorizedForPlayback
        )
        self.assertResultIsBOOL(AVFoundation.AVPlayerItem.isContentAuthorizedForPlayback)
        self.assertArgIsBlock(
            AVFoundation.AVPlayerItem.requestContentAuthorizationAsynchronouslyWithTimeoutInterval_completionHandler_,  # noqa: B950
            1,
            b"v",
        )
