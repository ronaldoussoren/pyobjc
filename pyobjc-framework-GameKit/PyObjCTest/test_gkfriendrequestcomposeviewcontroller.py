import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKFriendRequestComposeViewController(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKFriendRequestComposeViewControllerDelegate")
