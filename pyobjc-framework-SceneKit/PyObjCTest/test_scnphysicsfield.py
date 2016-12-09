from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    SCNFieldForceEvaluator = (SceneKit.SCNVector3.__typestr__
            + SceneKit.SCNVector3.__typestr__
            + SceneKit.SCNVector3.__typestr__
            + objc._C_FLT
            + objc._C_FLT
            + objc._C_DBL)

    class TestSCNPhysicsField (TestCase):
        def test_constants(self):
            self.assertEqual(SceneKit.SCNPhysicsFieldScopeInsideExtent, 0)
            self.assertEqual(SceneKit.SCNPhysicsFieldScopeOutsideExtent, 1)

        @min_os_level('10.10')
        def testMethods10_10(self):
            self.assertArgIsBOOL(SceneKit.SCNPhysicsField.setActive_, 0)
            self.assertResultIsBOOL(SceneKit.SCNPhysicsField.isActive)

            self.assertArgIsBOOL(SceneKit.SCNPhysicsField.setExclusive_, 0)
            self.assertResultIsBOOL(SceneKit.SCNPhysicsField.isExclusive)

            self.assertArgIsBOOL(SceneKit.SCNPhysicsField.setUsesEllipsoidalExtent_, 0)
            self.assertResultIsBOOL(SceneKit.SCNPhysicsField.usesEllipsoidalExtent)

            self.assertArgIsBlock(SceneKit.SCNPhysicsField.customFieldWithEvaluationBlock_, 0, SCNFieldForceEvaluator)


if __name__ == "__main__":
    main()
