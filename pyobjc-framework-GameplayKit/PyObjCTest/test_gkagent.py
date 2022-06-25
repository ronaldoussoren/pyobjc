from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKAgent(TestCase):
    def testProtocols(self):
        self.assertProtocolExists("GKAgentDelegate")

    def testMethods(self):
        self.assertResultIsBOOL(GameplayKit.GKAgent3D.rightHanded)
        self.assertArgIsBOOL(GameplayKit.GKAgent3D.setRightHanded_, 0)
