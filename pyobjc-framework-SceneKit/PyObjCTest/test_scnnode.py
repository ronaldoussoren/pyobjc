from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import SceneKit
from objc import simd


class TestSCNMaterialProperty(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SceneKit.SCNMovabilityHint)
        self.assertIsEnumType(SceneKit.SCNNodeFocusBehavior)

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

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultHasType(
            SceneKit.SCNNode.simdTransform, simd.simd_float4x4.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdPosition, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdRotation, simd.simd_float4.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdOrientation, simd.simd_quatf.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdEulerAngles, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdScale, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdPivot, simd.simd_float4x4.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdWorldPosition, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdWorldOrientation, simd.simd_quatf.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdWorldTransform, simd.simd_float4x4.__typestr__
        )

        self.assertArgHasType(
            SceneKit.SCNNode.setSimdTransform_, 0, simd.simd_float4x4.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.setSimdPosition_, 0, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.setSimdRotation_, 0, simd.simd_float4.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.setSimdOrientation_, 0, simd.simd_quatf.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.setSimdEulerAngles_, 0, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.setSimdScale_, 0, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.setSimdPivot_, 0, simd.simd_float4x4.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.setSimdWorldPosition_, 0, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.setSimdWorldOrientation_, 0, simd.simd_quatf.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.setSimdWorldTransform_, 0, simd.simd_float4x4.__typestr__
        )

        self.assertResultHasType(
            SceneKit.SCNNode.simdConvertPosition_toNode_, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.simdConvertPosition_toNode_,
            0,
            simd.simd_float3.__typestr__,
        )

        self.assertResultHasType(
            SceneKit.SCNNode.simdConvertPosition_fromNode_, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.simdConvertPosition_fromNode_,
            0,
            simd.simd_float3.__typestr__,
        )

        self.assertResultHasType(
            SceneKit.SCNNode.simdConvertVector_fromNode_, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.simdConvertVector_fromNode_,
            0,
            simd.simd_float3.__typestr__,
        )

        self.assertResultHasType(
            SceneKit.SCNNode.simdConvertVector_toNode_, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.simdConvertVector_toNode_, 0, simd.simd_float3.__typestr__
        )

        self.assertResultHasType(
            SceneKit.SCNNode.simdConvertTransform_toNode_,
            simd.simd_float4x4.__typestr__,
        )
        self.assertArgHasType(
            SceneKit.SCNNode.simdConvertTransform_toNode_,
            0,
            simd.simd_float4x4.__typestr__,
        )

        self.assertResultHasType(
            SceneKit.SCNNode.simdLocalUp, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdLocalRight, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdLocalFront, simd.simd_float3.__typestr__
        )

        self.assertResultHasType(
            SceneKit.SCNNode.simdWorldUp, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdWorldRight, simd.simd_float3.__typestr__
        )
        self.assertResultHasType(
            SceneKit.SCNNode.simdWorldFront, simd.simd_float3.__typestr__
        )

        self.assertArgHasType(
            SceneKit.SCNNode.simdLookAt_, 0, simd.simd_float3.__typestr__
        )

        self.assertArgHasType(
            SceneKit.SCNNode.simdLookAt_up_localFront_, 0, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.simdLookAt_up_localFront_, 1, simd.simd_float3.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.simdLookAt_up_localFront_, 2, simd.simd_float3.__typestr__
        )

        self.assertArgHasType(
            SceneKit.SCNNode.simdLocalTranslateBy_, 0, simd.simd_float3.__typestr__
        )

        self.assertArgHasType(
            SceneKit.SCNNode.simdLocalRotateBy_, 0, simd.simd_quatf.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.simdRotateBy_aroundTarget_, 0, simd.simd_quatf.__typestr__
        )
        self.assertArgHasType(
            SceneKit.SCNNode.simdRotateBy_aroundTarget_, 1, simd.simd_float3.__typestr__
        )

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        self.assertProtocolExists("SCNNodeRendererDelegate")
