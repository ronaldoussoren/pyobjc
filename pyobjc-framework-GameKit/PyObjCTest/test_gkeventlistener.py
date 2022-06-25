import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKEventListener(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKChallengeListener")
