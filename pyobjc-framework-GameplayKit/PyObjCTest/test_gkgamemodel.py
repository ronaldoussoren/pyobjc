from PyObjCTools.TestSupport import TestCase
import objc

import GameplayKit


class TestGKGameModelHelper(GameplayKit.NSObject):
    def value(self):
        return 1

    def setValue_(self, v):
        pass

    def playerId(self):
        return 1

    def setPlayerId_(self, v):
        pass

    def scoreForPlayer_(self, p):
        return 1

    def isWinForPlayer_(self, p):
        return 1

    def isLossForPlayer_(self, p):
        return 1


class TestGKGameModel(TestCase):
    def test_constants(self):
        self.assertEqual(GameplayKit.GKGameModelMaxScore, 1 << 24)
        self.assertEqual(GameplayKit.GKGameModelMinScore, -(1 << 24))

    def test_methods(self):
        self.assertResultHasType(TestGKGameModelHelper.value, objc._C_NSInteger)
        self.assertArgHasType(TestGKGameModelHelper.setValue_, 0, objc._C_NSInteger)

        self.assertResultHasType(TestGKGameModelHelper.playerId, objc._C_NSInteger)
        self.assertArgHasType(TestGKGameModelHelper.setPlayerId_, 0, objc._C_NSInteger)

        self.assertResultHasType(
            TestGKGameModelHelper.scoreForPlayer_, objc._C_NSInteger
        )
        self.assertResultIsBOOL(TestGKGameModelHelper.isWinForPlayer_)
        self.assertResultIsBOOL(TestGKGameModelHelper.isLossForPlayer_)

    def test_protocols(self):
        self.assertProtocolExists("GKGameModelUpdate", GameplayKit)
        self.assertProtocolExists("GKGameModelPlayer", GameplayKit)
        self.assertProtocolExists("GKGameModel", GameplayKit)
