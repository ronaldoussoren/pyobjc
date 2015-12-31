from PyObjCTools.TestSupport import *
import objc

import SceneKit

class TestSCNMaterialProperty (TestCase):
    def testConstants(self):
        self.assertIsInstance(SceneKit.SCNModelTransform, unicode)
        self.assertIsInstance(SceneKit.SCNViewTransform, unicode)
        self.assertIsInstance(SceneKit.SCNProjectionTransform, unicode)
        self.assertIsInstance(SceneKit.SCNNormalTransform, unicode)
        self.assertIsInstance(SceneKit.SCNModelViewTransform, unicode)
        self.assertIsInstance(SceneKit.SCNModelViewProjectionTransform, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNNode.isHidden)
        self.assertArgIsBOOL(SceneKit.SCNNode.setHidden_, 0)

        self.assertArgIsBOOL(SceneKit.SCNNode.childNodeWithName_recursively_, 1)

        self.assertArgIsBlock(SceneKit.SCNNode.childNodesPassingTest_, 0, b'Z@o^Z')

    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(SceneKit.SCNNode.castsShadow)
        self.assertArgIsBOOL(SceneKit.SCNNode.setCastsShadow_, 0)

        self.assertArgIsBlock(SceneKit.SCNNode.enumerateChildNodesUsingBlock_, 0, b'v@o^Z')

        self.assertResultIsBOOL(SceneKit.SCNNode.isPaused)
        self.assertArgIsBOOL(SceneKit.SCNNode.setPaused_, 0)

    def testProtocolObjects(self):
        objc.protocolNamed('SCNNodeRendererDelegate')

if __name__ == "__main__":
    main()
