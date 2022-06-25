from PyObjCTools.TestSupport import TestCase
import GameplayKit  # noqa: F401


class TestGKAgent(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKSceneRootNodeType")
