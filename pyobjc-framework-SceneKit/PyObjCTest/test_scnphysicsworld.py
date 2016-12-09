from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:
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

        @min_os_level('10.12')
        def test_constants10_12(self):
            self.assertIsInstance(SceneKit.SCNPhysicsTestOptionBackfaceCulling, unicode)

            self.assertIs(SceneKit.SCNPhysicsTestOptionCollisionBitMask, SceneKit.SCNPhysicsTestCollisionBitMaskKey)
            self.assertIs(SceneKit.SCNPhysicsTestOptionSearchMode, SceneKit.SCNPhysicsTestSearchModeKey)
            self.assertIs(SceneKit.SCNPhysicsTestOptionBackfaceCulling, SceneKit.SCNPhysicsTestBackfaceCullingKey)


        @min_sdk_level('10.10')
        def testProtocols(self):
            objc.protocolNamed('SCNPhysicsContactDelegate')


if __name__ == "__main__":
    main()
