from PyObjCTools.TestSupport import TestCase, min_sdk_level
import GameplayKit  # noqa: F401


class TestGKAgent(TestCase):
    @min_sdk_level("10.12")
    def testProtocols(self):
        self.assertProtocolExists("GKSceneRootNodeType")
