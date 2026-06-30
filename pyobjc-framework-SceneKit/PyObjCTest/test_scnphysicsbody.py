import sys

from PyObjCTools.TestSupport import TestCase, min_os_level


import SceneKit


class TestSCNPhysicsBody(TestCase):
    def test_enums(self):
        self.assertIsEnumType(SceneKit.SCNPhysicsBodyType)
        self.assertEqual(SceneKit.SCNPhysicsBodyTypeStatic, 0)
        self.assertEqual(SceneKit.SCNPhysicsBodyTypeDynamic, 1)
        self.assertEqual(SceneKit.SCNPhysicsBodyTypeKinematic, 2)

        self.assertIsEnumType(SceneKit.SCNPhysicsCollisionCategory)
        self.assertEqual(SceneKit.SCNPhysicsCollisionCategoryDefault, 1 << 0)
        self.assertEqual(SceneKit.SCNPhysicsCollisionCategoryStatic, 1 << 1)
        self.assertEqual(SceneKit.SCNPhysicsCollisionCategoryAll, (sys.maxsize * 2) + 1)

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(SceneKit.SCNPhysicsBody.isResting)

        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.setAllowsResting_, 0)
        self.assertResultIsBOOL(SceneKit.SCNPhysicsBody.allowsResting)

        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.applyForce_impulse_, 1)
        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.applyForce_atPosition_impulse_, 2)
        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.applyTorque_impulse_, 1)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.setUsesDefaultMomentOfInertia_, 0)
        self.assertResultIsBOOL(SceneKit.SCNPhysicsBody.usesDefaultMomentOfInertia)

        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.setAffectedByGravity_, 0)
        self.assertResultIsBOOL(SceneKit.SCNPhysicsBody.isAffectedByGravity)

    @min_os_level("10.14")
    def test_methods10_14(self):
        self.assertArgIsBOOL(SceneKit.SCNPhysicsBody.setResting_, 0)
