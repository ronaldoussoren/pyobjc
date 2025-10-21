from PyObjCTools.TestSupport import TestCase, min_os_level
import GameKit


class TestGKAccessPoint(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameKit.GKAccessPointLocation)

    def test_constants(self):
        self.assertEqual(GameKit.GKAccessPointLocationTopLeading, 0)
        self.assertEqual(GameKit.GKAccessPointLocationTopTrailing, 1)
        self.assertEqual(GameKit.GKAccessPointLocationBottomLeading, 2)
        self.assertEqual(GameKit.GKAccessPointLocationBottomTrailing, 3)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertResultIsBOOL(GameKit.GKAccessPoint.isActive)
        self.assertArgIsBOOL(GameKit.GKAccessPoint.setActive_, 0)

        self.assertResultIsBOOL(GameKit.GKAccessPoint.isVisible)
        self.assertResultIsBOOL(GameKit.GKAccessPoint.isPresentingGameCenter)

        self.assertResultIsBOOL(GameKit.GKAccessPoint.showHighlights)
        self.assertArgIsBOOL(GameKit.GKAccessPoint.setShowHighlights_, 0)

        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithHandler_, 0, b"v"
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithState_handler_, 1, b"v"
        )

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithAchievementID_handler_, 1, b"v"
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithLeaderboardSetID_handler_,
            1,
            b"v",
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithLeaderboardID_playerScope_timeScope_handler_,
            3,
            b"v",
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithPlayer_handler_, 1, b"v"
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointForPlayTogetherWithHandler_, 0, b"v"
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointForChallengesWithHandler_, 0, b"v"
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithChallengeDefinitionID_handler_,
            1,
            b"v",
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithGameActivityDefinitionID_handler_,
            1,
            b"v",
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointWithGameActivity_handler_, 1, b"v"
        )
        self.assertArgIsBlock(
            GameKit.GKAccessPoint.triggerAccessPointForFriendingWithHandler_, 0, b"v"
        )
