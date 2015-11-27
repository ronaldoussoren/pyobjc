from PyObjCTools.TestSupport import *
import objc
import sys

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


if __name__ == "__main__":
    main()
