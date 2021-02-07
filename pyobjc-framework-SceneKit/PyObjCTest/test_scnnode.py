import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import SceneKit


class TestSCNMaterialProperty(TestCase):
    def testConstants(self):
        self.assertIsInstance(SceneKit.SCNModelTransform, str)
        self.assertIsInstance(SceneKit.SCNViewTransform, str)
        self.assertIsInstance(SceneKit.SCNProjectionTransform, str)
        self.assertIsInstance(SceneKit.SCNNormalTransform, str)
        self.assertIsInstance(SceneKit.SCNModelViewTransform, str)
        self.assertIsInstance(SceneKit.SCNModelViewProjectionTransform, str)

        self.assertEqual(SceneKit.SCNMovabilityHintFixed, 0)
        self.assertEqual(SceneKit.SCNMovabilityHintMovable, 1)

        self.assertEqual(SceneKit.SCNNodeFocusBehaviorNone, 0)
        self.assertEqual(SceneKit.SCNNodeFocusBehaviorOccluding, 1)
        self.assertEqual(SceneKit.SCNNodeFocusBehaviorFocusable, 2)

    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNNode.isHidden)
        self.assertArgIsBOOL(SceneKit.SCNNode.setHidden_, 0)

        self.assertArgIsBOOL(SceneKit.SCNNode.childNodeWithName_recursively_, 1)

        self.assertArgIsBlock(SceneKit.SCNNode.childNodesPassingTest_, 0, b"Z@o^Z")

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(SceneKit.SCNNode.castsShadow)
        self.assertArgIsBOOL(SceneKit.SCNNode.setCastsShadow_, 0)

        self.assertArgIsBlock(
            SceneKit.SCNNode.enumerateChildNodesUsingBlock_, 0, b"v@o^Z"
        )

        self.assertResultIsBOOL(SceneKit.SCNNode.isPaused)
        self.assertArgIsBOOL(SceneKit.SCNNode.setPaused_, 0)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(
            SceneKit.SCNNode.enumerateHierarchyUsingBlock_, 0, b"v@o^Z"
        )

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        objc.protocolNamed("SCNNodeRendererDelegate")
