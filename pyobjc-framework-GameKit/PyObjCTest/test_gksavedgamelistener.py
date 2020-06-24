import GameKit  # noqa: F401
from PyObjCTools.TestSupport import TestCase
import objc


class TestGKSavedGameListener(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKSavedGameListener")
