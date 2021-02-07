import GameKit  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase


class TestGKLeaderboardViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKLeaderboardViewControllerDelegate")
