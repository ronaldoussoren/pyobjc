import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKSavedGameListener(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("GKSavedGameListener", GameKit)
