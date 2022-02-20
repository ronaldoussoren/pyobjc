import objc
from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKNode(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SpriteKit.SKBlendMode)
        self.assertIsEnumType(SpriteKit.SKNodeFocusBehavior)

    @min_os_level("10.9")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKBlendModeAlpha, 0)
        self.assertEqual(SpriteKit.SKBlendModeAdd, 1)
        self.assertEqual(SpriteKit.SKBlendModeSubtract, 2)
        self.assertEqual(SpriteKit.SKBlendModeMultiply, 3)
        self.assertEqual(SpriteKit.SKBlendModeMultiplyX2, 4)
        self.assertEqual(SpriteKit.SKBlendModeScreen, 5)
        self.assertEqual(SpriteKit.SKBlendModeReplace, 6)

    @min_os_level("10.9")
    def testMethods(self):
        self.assertIsInstance(SpriteKit.SKNode, objc.objc_class)

        self.assertArgIsBOOL(SpriteKit.SKNode.setPaused_, 0)
        self.assertResultIsBOOL(SpriteKit.SKNode.isPaused)
        self.assertArgIsBOOL(SpriteKit.SKNode.setHidden_, 0)
        self.assertResultIsBOOL(SpriteKit.SKNode.isHidden)
        self.assertArgIsBOOL(SpriteKit.SKNode.setUserInteractionEnabled_, 0)
        self.assertResultIsBOOL(SpriteKit.SKNode.isUserInteractionEnabled)
        self.assertResultIsBOOL(SpriteKit.SKNode.inParentHierarchy_)
        self.assertResultIsBOOL(SpriteKit.SKNode.hasActions)
        self.assertResultIsBOOL(SpriteKit.SKNode.containsPoint_)
        self.assertResultIsBOOL(SpriteKit.SKNode.intersectsNode_)

        self.assertArgIsBlock(
            SpriteKit.SKNode.enumerateChildNodesWithName_usingBlock_, 1, b"v@o^Z"
        )
        self.assertArgIsBlock(SpriteKit.SKNode.runAction_completion_, 1, b"v")

    @min_os_level("10.14")
    def testMethods10_14(self):
        self.assertArgIsOut(
            SpriteKit.SKNode.nodeWithFileNamed_securelyWithClasses_andError_, 2
        )
