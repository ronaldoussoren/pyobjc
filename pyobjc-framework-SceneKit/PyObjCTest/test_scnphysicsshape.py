from PyObjCTools.TestSupport import *
import objc
import sys

if os_level_key(os_release()) < os_level_key('10.12') or sys.maxsize >= 2**32:

    import SceneKit

    class TestSCNPhysicsShape (TestCase):
        @min_os_level('10.10')
        def test_constants10_10(self):
            self.assertIsInstance(SceneKit.SCNPhysicsShapeTypeKey, unicode)

            self.assertIsInstance(SceneKit.SCNPhysicsShapeTypeBoundingBox, unicode)
            self.assertIsInstance(SceneKit.SCNPhysicsShapeTypeConvexHull, unicode)
            self.assertIsInstance(SceneKit.SCNPhysicsShapeTypeConcavePolyhedron, unicode)

            self.assertIsInstance(SceneKit.SCNPhysicsShapeKeepAsCompoundKey, unicode)

            self.assertIsInstance(SceneKit.SCNPhysicsShapeScaleKey, unicode)

        @min_os_level('10.12')
        def test_constants10_12(self):
            self.assertIsInstance(SceneKit.SCNPhysicsShapeOptionCollisionMargin, unicode)

            self.assertIs(SceneKit.SCNPhysicsShapeOptionType, SceneKit.SCNPhysicsShapeTypeKey)
            self.assertIs(SceneKit.SCNPhysicsShapeOptionKeepAsCompound, SceneKit.SCNPhysicsShapeKeepAsCompoundKey)
            self.assertIs(SceneKit.SCNPhysicsShapeOptionScale, SceneKit.SCNPhysicsShapeScaleKey)


if __name__ == "__main__":
    main()
