import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKLeaderboardViewController(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKLeaderboardViewControllerDelegate")
