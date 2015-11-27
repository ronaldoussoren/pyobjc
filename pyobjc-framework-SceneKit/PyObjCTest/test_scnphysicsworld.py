from PyObjCTools.TestSupport import *
import objc
import sys

import SceneKit

class TestSCNPhysicsShape (TestCase):
    @min_os_level('10.10')
    def test_constants10_10(self):
        self.assertIsInstance(SceneKit.SCNPhysicsTestCollisionBitMaskKey, unicode)
        self.assertIsInstance(SceneKit.SCNPhysicsTestSearchModeKey, unicode)
        self.assertIsInstance(SceneKit.SCNPhysicsTestBackfaceCullingKey, unicode)

        self.assertIsInstance(SceneKit.SCNPhysicsTestSearchModeAny, unicode)
        self.assertIsInstance(SceneKit.SCNPhysicsTestSearchModeClosest, unicode)
        self.assertIsInstance(SceneKit.SCNPhysicsTestSearchModeAll, unicode)

    @min_sdk_level('10.10')
    def testProtocols(self):
        objc.protocolNamed('SCNPhysicsContactDelegate')


if __name__ == "__main__":
    main()
