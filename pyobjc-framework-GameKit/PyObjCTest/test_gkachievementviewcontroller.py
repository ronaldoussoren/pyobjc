import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKAchievementViewController(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKAchievementViewControllerDelegate")
