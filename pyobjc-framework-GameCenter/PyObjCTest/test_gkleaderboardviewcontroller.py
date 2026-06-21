from PyObjCTools.TestSupport import TestCase, min_os_level

import GameCenter  # noqa: F401


class TestGKLeaderboardViewController(TestCase):
    @min_os_level("10.8")
    def test_protocols(self):
        self.assertProtocolExists("GKLeaderboardViewControllerDelegate", GameCenter)
