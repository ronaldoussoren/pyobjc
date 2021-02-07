import GameKit  # noqa: F401
import objc
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestGKGameSessionEventListener(TestCase):
    @min_sdk_level("10.12")
    def testProtocols(self):
        objc.protocolNamed("GKGameSessionEventListener")
