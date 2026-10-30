import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKLeaderboardViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKLeaderboardViewControllerDelegate", GameKit)
