import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestGKError(TestCase):
    def testConstants(self):

        self.assertEqual(GameKit.GKGameSessionErrorUnknown, 1)
        self.assertEqual(GameKit.GKGameSessionErrorNotAuthenticated, 2)
        self.assertEqual(GameKit.GKGameSessionErrorSessionConflict, 3)
        self.assertEqual(GameKit.GKGameSessionErrorSessionNotShared, 4)
        self.assertEqual(GameKit.GKGameSessionErrorConnectionCancelledByUser, 5)
        self.assertEqual(GameKit.GKGameSessionErrorConnectionFailed, 6)
        self.assertEqual(GameKit.GKGameSessionErrorSessionHasMaxConnectedPlayers, 7)
        self.assertEqual(GameKit.GKGameSessionErrorSendDataNotConnected, 8)
        self.assertEqual(GameKit.GKGameSessionErrorSendDataNoRecipients, 9)
        self.assertEqual(GameKit.GKGameSessionErrorSendDataNotReachable, 10)
        self.assertEqual(GameKit.GKGameSessionErrorSendRateLimitReached, 11)
        self.assertEqual(GameKit.GKGameSessionErrorBadContainer, 12)
        self.assertEqual(GameKit.GKGameSessionErrorCloudQuotaExceeded, 13)
        self.assertEqual(GameKit.GKGameSessionErrorNetworkFailure, 14)
        self.assertEqual(GameKit.GKGameSessionErrorCloudDriveDisabled, 15)
        self.assertEqual(GameKit.GKGameSessionErrorInvalidSession, 16)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(GameKit.GKGameSessionErrorDomain, str)
