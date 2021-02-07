import GameKit  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase


class TestGKEventListener(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKChallengeListener")
