from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc

import SceneKit

_C_SCNVector3 = (
    b"{SCNVector3=" + objc._C_CGFloat + objc._C_CGFloat + objc._C_CGFloat + b"}"
)
_C_SCNVector4 = (
    b"{SCNVector4="
    + objc._C_CGFloat
    + objc._C_CGFloat
    + objc._C_CGFloat
    + objc._C_CGFloat
    + b"}"
)


class TestSCNConstraint(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(SceneKit.SCNBillboardAxis)

    def testConstants(self):
        self.assertEqual(SceneKit.SCNBillboardAxisX, 0x1 << 0)
        self.assertEqual(SceneKit.SCNBillboardAxisY, 0x1 << 1)
        self.assertEqual(SceneKit.SCNBillboardAxisZ, 0x1 << 2)

        self.assertEqual(
            SceneKit.SCNBillboardAxisAll,
            SceneKit.SCNBillboardAxisX
            | SceneKit.SCNBillboardAxisY
            | SceneKit.SCNBillboardAxisZ,
        )

    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNLookAtConstraint.gimbalLockEnabled)
        self.assertArgIsBOOL(SceneKit.SCNLookAtConstraint.setGimbalLockEnabled_, 0)

        self.assertArgIsBOOL(
            SceneKit.SCNTransformConstraint.transformConstraintInWorldSpace_withBlock_,
            0,
        )
        self.assertArgIsBlock(
            SceneKit.SCNTransformConstraint.transformConstraintInWorldSpace_withBlock_,
            1,
            SceneKit.SCNMatrix4.__typestr__ + b"@" + SceneKit.SCNMatrix4.__typestr__,
        )

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(SceneKit.SCNConstraint.isEnabled)
        self.assertArgIsBOOL(SceneKit.SCNConstraint.setEnabled_, 0)

        self.assertResultIsBOOL(SceneKit.SCNConstraint.isIncremental)
        self.assertArgIsBOOL(SceneKit.SCNConstraint.setIncremental_, 0)

        self.assertArgIsBOOL(
            SceneKit.SCNTransformConstraint.positionConstraintInWorldSpace_withBlock_, 0
        )
        self.assertArgIsBlock(
            SceneKit.SCNTransformConstraint.positionConstraintInWorldSpace_withBlock_,
            1,
            _C_SCNVector3 + objc._C_ID + _C_SCNVector3,
        )
        self.assertArgIsBlock(
            SceneKit.SCNTransformConstraint.orientationConstraintInWorldSpace_withBlock_,
            1,
            _C_SCNVector4 + objc._C_ID + _C_SCNVector4,
        )

        self.assertResultIsBOOL(SceneKit.SCNReplicatorConstraint.replicatesOrientation)
        self.assertResultIsBOOL(SceneKit.SCNReplicatorConstraint.replicatesPosition)
        self.assertResultIsBOOL(SceneKit.SCNReplicatorConstraint.replicatesScale)
        self.assertArgIsBOOL(
            SceneKit.SCNReplicatorConstraint.setReplicatesOrientation_, 0
        )
        self.assertArgIsBOOL(SceneKit.SCNReplicatorConstraint.setReplicatesPosition_, 0)
        self.assertArgIsBOOL(SceneKit.SCNReplicatorConstraint.setReplicatesScale_, 0)

    @min_sdk_level("10.13")
    def testProtocols(self):
        self.assertProtocolExists("SCNAvoidOccluderConstraintDelegate")
