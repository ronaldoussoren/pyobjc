from PyObjCTools.TestSupport import TestCase

import GameCenter  # noqa: F401


class TestGKFriendRequestComposeViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists(
            "GKFriendRequestComposeViewControllerDelegate", GameCenter
        )
