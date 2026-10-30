import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKEventListener(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKChallengeListener", GameKit)
