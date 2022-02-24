import GameKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestGKMatchmakerViewController(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKMatchmakingMode)

    def test_constants(self):
        self.assertEqual(GameKit.GKMatchmakingModeDefault, 0)
        self.assertEqual(GameKit.GKMatchmakingModeNearbyOnly, 1)
        self.assertEqual(GameKit.GKMatchmakingModeAutomatchOnly, 2)
        self.assertEqual(GameKit.GKMatchmakingModeInviteOnly, 3)

    def testMethods(self):
        self.assertResultIsBOOL(GameKit.GKMatchmakerViewController.isHosted)
        self.assertArgIsBOOL(GameKit.GKMatchmakerViewController.setHosted_, 0)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBOOL(
            GameKit.GKMatchmakerViewController.setHostedPlayer_connected_, 1
        )

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBOOL(
            GameKit.GKMatchmakerViewController.setHostedPlayer_didConnect_, 1
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(
            GameKit.GKMatchmakerViewController.canStartWithMinimumPlayers
        )
        self.assertArgIsBOOL(
            GameKit.GKMatchmakerViewController.setCanStartWithMinimumPlayers_, 0
        )

    def testProtocols(self):
        objc.protocolNamed("GKMatchmakerViewControllerDelegate")
