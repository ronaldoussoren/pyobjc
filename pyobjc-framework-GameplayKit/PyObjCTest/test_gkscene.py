from PyObjCTools.TestSupport import TestCase
import objc
import GameplayKit  # noqa: F401


class TestGKAgent(TestCase):
    def testProtocols(self):
        objc.protocolNamed("GKSceneRootNodeType")
