from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKLeaderboardViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKLeaderboardViewControllerDelegate", GameCenter)
