from PyObjCTools.TestSupport import TestCase

import GameCenter


class TestGKChallengesViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKChallengesViewControllerDelegate", GameCenter)
