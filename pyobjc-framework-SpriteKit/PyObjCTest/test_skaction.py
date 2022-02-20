import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import SpriteKit


SKActionTimingFunction = objc._C_FLT + objc._C_FLT


class TestSKAction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SpriteKit.SKActionTimingMode)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKActionTimingLinear, 0)
        self.assertEqual(SpriteKit.SKActionTimingEaseIn, 1)
        self.assertEqual(SpriteKit.SKActionTimingEaseOut, 2)
        self.assertEqual(SpriteKit.SKActionTimingEaseInEaseOut, 3)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertIsInstance(SpriteKit.SKAction, objc.objc_class)

        self.assertArgIsBOOL(
            SpriteKit.SKAction.rotateToAngle_duration_shortestUnitArc_, 2
        )
        self.assertArgIsBOOL(
            SpriteKit.SKAction.animateWithTextures_timePerFrame_resize_restore_, 2
        )
        self.assertArgIsBOOL(
            SpriteKit.SKAction.animateWithTextures_timePerFrame_resize_restore_, 3
        )
        self.assertArgIsBOOL(
            SpriteKit.SKAction.playSoundFileNamed_waitForCompletion_, 1
        )
        self.assertArgIsBOOL(
            SpriteKit.SKAction.followPath_asOffset_orientToPath_duration_, 1
        )
        self.assertArgIsBOOL(
            SpriteKit.SKAction.followPath_asOffset_orientToPath_duration_, 2
        )
        self.assertArgIsSEL(SpriteKit.SKAction.performSelector_onTarget_, 0, b"v@:")

        self.assertArgIsBlock(
            SpriteKit.SKAction.customActionWithDuration_actionBlock_,
            1,
            b"v@" + objc._C_CGFloat,
        )

    @expectedFailure
    def testMethods_dispatch(self):
        self.fail("SpriteKit.SKAction.runBlock_queue_")
        self.fail("SpriteKit.SKAction.runBlock_")

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBOOL(
            SpriteKit.SKAction.followPath_asOffset_orientToPath_speed_, 1
        )
        self.assertArgIsBOOL(
            SpriteKit.SKAction.followPath_asOffset_orientToPath_speed_, 2
        )
        self.assertArgIsBOOL(SpriteKit.SKAction.setTexture_resize_, 1)
        self.assertResultIsBlock(
            SpriteKit.SKAction.timingFunction, SKActionTimingFunction
        )
        self.assertArgIsBlock(
            SpriteKit.SKAction.setTimingFunction_, 0, SKActionTimingFunction
        )
