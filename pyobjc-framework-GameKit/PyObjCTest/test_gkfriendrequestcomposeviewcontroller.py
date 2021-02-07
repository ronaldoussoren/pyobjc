import GameKit  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase


class TestGKFriendRequestComposeViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKFriendRequestComposeViewControllerDelegate")
