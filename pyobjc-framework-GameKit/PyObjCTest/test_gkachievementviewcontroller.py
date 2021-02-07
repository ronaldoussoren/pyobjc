import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase
import objc


class TestGKAchievementViewController(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKAchievementViewControllerDelegate")
