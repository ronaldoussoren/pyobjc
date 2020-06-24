import GameKit  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase


class TestGKAchievementViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKChallengesViewControllerDelegate")
