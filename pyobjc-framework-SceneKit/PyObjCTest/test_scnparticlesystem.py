from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    # FIXME: needs smarter metadata than what PyObjCTest supports!
    SCNParticleEventBlock = b'v^^v^' + objc._C_NSUInteger + b'^' + objc._C_NSUInteger + objc._C_NSInteger
    SCNParticleModifierBlock = b'v^^v^' + objc._C_NSUInteger + objc._C_NSInteger + objc._C_NSInteger + objc._C_FLT


    class TestSCNParticleSystem (TestCase):
        @min_os_level('10.10')
        def testConstants10_10(self):
            self.assertIsInstance(SceneKit.SCNParticlePropertyPosition, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyAngle, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyRotationAxis, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyVelocity, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyAngularVelocity, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyLife, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyColor, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyOpacity, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertySize, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyFrame, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyFrameRate, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyBounce, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyCharge, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyFriction, unicode)

            self.assertIsInstance(SceneKit.SCNParticlePropertyContactPoint, unicode)
            self.assertIsInstance(SceneKit.SCNParticlePropertyContactNormal, unicode)


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

        @min_os_level('10.10')
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

            self.assertArgIsBlock(SceneKit.SCNParticleSystem.handleEvent_forProperties_withBlock_, 2, SCNParticleEventBlock)
            self.assertArgIsBlock(SceneKit.SCNParticleSystem.addModifierForProperties_atStage_withBlock_, 2, SCNParticleModifierBlock)


if __name__ == "__main__":
    main()
