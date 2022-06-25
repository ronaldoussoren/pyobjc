import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import SceneKit

SCNActionTimingFunction = b"ff"


class TestSCNActionHelper(SceneKit.NSObject):
    def runAction_completionHandler_(self, a, h):
        pass

    def runAction_forKey_completionHandler_(self, a, k, h):
        pass

    def hasActions(self):
        return 1


class TestSCNAction(TestCase):
    @min_os_level("10.10")
    def test_constants(self):
        self.assertEqual(SceneKit.SCNActionTimingModeLinear, 0)
        self.assertEqual(SceneKit.SCNActionTimingModeEaseIn, 1)
        self.assertEqual(SceneKit.SCNActionTimingModeEaseOut, 2)
        self.assertEqual(SceneKit.SCNActionTimingModeEaseInEaseOut, 3)

    @min_os_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("SCNActionable")

    @min_os_level("10.10")
    def testMethods(self):
        self.assertResultIsBlock(
            SceneKit.SCNAction.timingFunction, SCNActionTimingFunction
        )
        self.assertArgIsBlock(
            SceneKit.SCNAction.setTimingFunction_, 0, SCNActionTimingFunction
        )
        self.assertArgIsBOOL(
            SceneKit.SCNAction.rotateToX_y_z_duration_shortestUnitArc_, 4
        )
        self.assertArgIsBlock(SceneKit.SCNAction.runBlock_, 0, b"v@")
        self.assertArgIsBlock(SceneKit.SCNAction.runBlock_queue_, 0, b"v@")
        self.assertArgIsBlock(
            SceneKit.SCNAction.customActionWithDuration_actionBlock_,
            1,
            b"v@" + objc._C_CGFloat,
        )

        self.assertArgIsBlock(TestSCNActionHelper.runAction_completionHandler_, 1, b"v")
        self.assertArgIsBlock(
            TestSCNActionHelper.runAction_forKey_completionHandler_, 2, b"v"
        )
        self.assertResultIsBOOL(TestSCNActionHelper.hasActions)

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBOOL(SceneKit.SCNAction.playAudioSource_waitForCompletion_, 1)
