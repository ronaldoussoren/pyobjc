import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import SceneKit


class TestSCNPhysicsShape(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(SceneKit.SCNPhysicsTestOption, str)
        self.assertIsTypedEnum(SceneKit.SCNPhysicsTestSearchMode, str)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(SceneKit.SCNPhysicsTestCollisionBitMaskKey, str)
        self.assertIsInstance(SceneKit.SCNPhysicsTestSearchModeKey, str)
        self.assertIsInstance(SceneKit.SCNPhysicsTestBackfaceCullingKey, str)

        self.assertIsInstance(SceneKit.SCNPhysicsTestSearchModeAny, str)
        self.assertIsInstance(SceneKit.SCNPhysicsTestSearchModeClosest, str)
        self.assertIsInstance(SceneKit.SCNPhysicsTestSearchModeAll, str)

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(SceneKit.SCNPhysicsTestOptionBackfaceCulling, str)

        self.assertIs(
            SceneKit.SCNPhysicsTestOptionCollisionBitMask,
            SceneKit.SCNPhysicsTestCollisionBitMaskKey,
        )
        self.assertIs(
            SceneKit.SCNPhysicsTestOptionSearchMode,
            SceneKit.SCNPhysicsTestSearchModeKey,
        )
        self.assertIs(
            SceneKit.SCNPhysicsTestOptionBackfaceCulling,
            SceneKit.SCNPhysicsTestBackfaceCullingKey,
        )

    @min_sdk_level("10.10")
    def testProtocols(self):
        objc.protocolNamed("SCNPhysicsContactDelegate")
