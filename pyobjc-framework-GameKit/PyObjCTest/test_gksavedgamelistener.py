import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase


class TestGKSavedGameListener(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKSavedGameListener")
