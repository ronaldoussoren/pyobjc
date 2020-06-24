import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


import SceneKit

# FIXME: needs smarter metadata than what PyObjCTest supports!
SCNParticleEventBlock = (
    b"v^^v^" + objc._C_NSUInteger + b"^" + objc._C_NSUInteger + objc._C_NSInteger
)
SCNParticleModifierBlock = (
    b"v^^v^" + objc._C_NSUInteger + objc._C_NSInteger + objc._C_NSInteger + objc._C_FLT
)


class TestSCNParticleSystem(TestCase):
    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(SceneKit.SCNParticlePropertyPosition, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyAngle, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyRotationAxis, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyVelocity, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyAngularVelocity, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyLife, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyColor, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyOpacity, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertySize, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyFrame, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyFrameRate, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyBounce, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyCharge, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyFriction, str)

        self.assertIsInstance(SceneKit.SCNParticlePropertyContactPoint, str)
        self.assertIsInstance(SceneKit.SCNParticlePropertyContactNormal, str)

        self.assertEqual(SceneKit.SCNParticleSortingModeNone, 0)
        self.assertEqual(SceneKit.SCNParticleSortingModeProjectedDepth, 1)
        self.assertEqual(SceneKit.SCNParticleSortingModeDistance, 2)
        self.assertEqual(SceneKit.SCNParticleSortingModeOldestFirst, 3)
        self.assertEqual(SceneKit.SCNParticleSortingModeYoungestFirst, 4)

        self.assertEqual(SceneKit.SCNParticleBlendModeAdditive, 0)
        self.assertEqual(SceneKit.SCNParticleBlendModeSubtract, 1)
        self.assertEqual(SceneKit.SCNParticleBlendModeMultiply, 2)
        self.assertEqual(SceneKit.SCNParticleBlendModeScreen, 3)
        self.assertEqual(SceneKit.SCNParticleBlendModeAlpha, 4)
        self.assertEqual(SceneKit.SCNParticleBlendModeReplace, 5)

        self.assertEqual(SceneKit.SCNParticleOrientationModeBillboardScreenAligned, 0)
        self.assertEqual(SceneKit.SCNParticleOrientationModeBillboardViewAligned, 1)
        self.assertEqual(SceneKit.SCNParticleOrientationModeFree, 2)
        self.assertEqual(SceneKit.SCNParticleOrientationModeBillboardYAligned, 3)

        self.assertEqual(SceneKit.SCNParticleBirthLocationSurface, 0)
        self.assertEqual(SceneKit.SCNParticleBirthLocationVolume, 1)
        self.assertEqual(SceneKit.SCNParticleBirthLocationVertex, 2)

        self.assertEqual(SceneKit.SCNParticleBirthDirectionConstant, 0)
        self.assertEqual(SceneKit.SCNParticleBirthDirectionSurfaceNormal, 1)
        self.assertEqual(SceneKit.SCNParticleBirthDirectionRandom, 2)

        self.assertEqual(SceneKit.SCNParticleImageSequenceAnimationModeRepeat, 0)
        self.assertEqual(SceneKit.SCNParticleImageSequenceAnimationModeClamp, 1)
        self.assertEqual(SceneKit.SCNParticleImageSequenceAnimationModeAutoReverse, 2)

        self.assertEqual(SceneKit.SCNParticleInputModeOverLife, 0)
        self.assertEqual(SceneKit.SCNParticleInputModeOverDistance, 1)
        self.assertEqual(SceneKit.SCNParticleInputModeOverOtherProperty, 2)

        self.assertEqual(SceneKit.SCNParticleModifierStagePreDynamics, 0)
        self.assertEqual(SceneKit.SCNParticleModifierStagePostDynamics, 1)
        self.assertEqual(SceneKit.SCNParticleModifierStagePreCollision, 2)
        self.assertEqual(SceneKit.SCNParticleModifierStagePostCollision, 3)

        self.assertEqual(SceneKit.SCNParticleEventBirth, 0)
        self.assertEqual(SceneKit.SCNParticleEventDeath, 1)
        self.assertEqual(SceneKit.SCNParticleEventCollision, 2)

    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(SceneKit.SCNParticleSystem.loops)
        self.assertArgIsBOOL(SceneKit.SCNParticleSystem.setLoops_, 0)

        self.assertResultIsBOOL(SceneKit.SCNParticleSystem.isLocal)
        self.assertArgIsBOOL(SceneKit.SCNParticleSystem.setLocal_, 0)

        self.assertResultIsBOOL(SceneKit.SCNParticleSystem.isBlackPassEnabled)
        self.assertArgIsBOOL(SceneKit.SCNParticleSystem.setBlackPassEnabled_, 0)

        self.assertResultIsBOOL(SceneKit.SCNParticleSystem.isLightingEnabled)
        self.assertArgIsBOOL(SceneKit.SCNParticleSystem.setLightingEnabled_, 0)

        self.assertResultIsBOOL(SceneKit.SCNParticleSystem.affectedByGravity)
        self.assertArgIsBOOL(SceneKit.SCNParticleSystem.setAffectedByGravity_, 0)

        self.assertResultIsBOOL(SceneKit.SCNParticleSystem.affectedByPhysicsFields)
        self.assertArgIsBOOL(SceneKit.SCNParticleSystem.setAffectedByPhysicsFields_, 0)

        self.assertResultIsBOOL(SceneKit.SCNParticleSystem.particleDiesOnCollision)
        self.assertArgIsBOOL(SceneKit.SCNParticleSystem.setParticleDiesOnCollision_, 0)

        self.assertArgIsBlock(
            SceneKit.SCNParticleSystem.handleEvent_forProperties_withBlock_,
            2,
            SCNParticleEventBlock,
        )
        self.assertArgIsBlock(
            SceneKit.SCNParticleSystem.addModifierForProperties_atStage_withBlock_,
            2,
            SCNParticleModifierBlock,
        )
