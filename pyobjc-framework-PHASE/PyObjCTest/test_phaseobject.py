from PyObjCTools.TestSupport import TestCase
from objc import simd

import PHASE


class TestPHASEObject(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(PHASE.PHASEObject.addChild_error_)
        self.assertArgIsOut(PHASE.PHASEObject.addChild_error_, 1)

        self.assertResultHasType(PHASE.PHASEObject.right, simd.simd_float3.__typestr__)
        self.assertResultHasType(PHASE.PHASEObject.up, simd.simd_float3.__typestr__)
        self.assertResultHasType(
            PHASE.PHASEObject.forward, simd.simd_float3.__typestr__
        )

        self.assertResultHasType(
            PHASE.PHASEObject.transform, simd.simd_float4x4.__typestr__
        )
        self.assertArgHasType(
            PHASE.PHASEObject.setTransform_, 0, simd.simd_float4x4.__typestr__
        )

        self.assertResultHasType(
            PHASE.PHASEObject.worldTransform, simd.simd_float4x4.__typestr__
        )
        self.assertArgHasType(
            PHASE.PHASEObject.setWorldTransform_, 0, simd.simd_float4x4.__typestr__
        )
