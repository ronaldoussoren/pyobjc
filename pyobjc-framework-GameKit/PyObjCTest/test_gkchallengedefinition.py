from PyObjCTools.TestSupport import TestCase, min_os_level
import GameKit


class TestGKChallengeDefinition(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(GameKit.GKChallengeDefinition.isRepeatable)

        self.assertArgIsBlock(
            GameKit.GKChallengeDefinition.loadImageWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            GameKit.GKChallengeDefinition.loadChallengeDefinitionsWithCompletionHandler_,
            0,
            b"v@@",
        )
        self.assertArgIsBlock(
            GameKit.GKChallengeDefinition.hasActiveChallengesWithCompletionHandler,
            0,
            b"vZ@",
        )
