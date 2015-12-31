from PyObjCTools.TestSupport import *
import objc

import SceneKit

class TestSCNConstraint (TestCase):
    def testConstants(self):
        self.assertEqual(SceneKit.SCNBillboardAxisX, 0x1 << 0)
        self.assertEqual(SceneKit.SCNBillboardAxisY, 0x1 << 1)
        self.assertEqual(SceneKit.SCNBillboardAxisZ, 0x1 << 2)

        self.assertEqual(SceneKit.SCNBillboardAxisAll,
            SceneKit.SCNBillboardAxisX | SceneKit.SCNBillboardAxisY | SceneKit.SCNBillboardAxisZ)

    def testMethods(self):
        self.assertResultIsBOOL(SceneKit.SCNLookAtConstraint.gimbalLockEnabled)
        self.assertArgIsBOOL(SceneKit.SCNLookAtConstraint.setGimbalLockEnabled_, 0)

        self.assertArgIsBOOL(SceneKit.SCNTransformConstraint.transformConstraintInWorldSpace_withBlock_, 0)
        self.assertArgIsBlock(SceneKit.SCNTransformConstraint.transformConstraintInWorldSpace_withBlock_, 1,
            SceneKit.SCNMatrix4.__typestr__ + b'@' + SceneKit.SCNMatrix4.__typestr__)


if __name__ == "__main__":
    main()
