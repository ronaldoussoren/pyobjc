import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKFriendRequestComposeViewController(TestCase):
    def test_protocols(self):
        self.assertProtocolExists(
            "GKFriendRequestComposeViewControllerDelegate", GameKit
        )
