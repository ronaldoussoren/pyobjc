import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKAchievementViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKChallengesViewControllerDelegate", GameKit)
