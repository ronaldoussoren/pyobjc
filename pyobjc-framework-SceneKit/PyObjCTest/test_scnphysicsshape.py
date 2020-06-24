from PyObjCTools.TestSupport import TestCase, min_os_level


import SceneKit


class TestSCNPhysicsShape(TestCase):
    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(SceneKit.SCNPhysicsShapeTypeKey, str)

        self.assertIsInstance(SceneKit.SCNPhysicsShapeTypeBoundingBox, str)
        self.assertIsInstance(SceneKit.SCNPhysicsShapeTypeConvexHull, str)
        self.assertIsInstance(SceneKit.SCNPhysicsShapeTypeConcavePolyhedron, str)

        self.assertIsInstance(SceneKit.SCNPhysicsShapeKeepAsCompoundKey, str)

        self.assertIsInstance(SceneKit.SCNPhysicsShapeScaleKey, str)

    @min_os_level("10.12")
    def test_constants10_12(self):
        self.assertIsInstance(SceneKit.SCNPhysicsShapeOptionCollisionMargin, str)

        self.assertIs(
            SceneKit.SCNPhysicsShapeOptionType, SceneKit.SCNPhysicsShapeTypeKey
        )
        self.assertIs(
            SceneKit.SCNPhysicsShapeOptionKeepAsCompound,
            SceneKit.SCNPhysicsShapeKeepAsCompoundKey,
        )
        self.assertIs(
            SceneKit.SCNPhysicsShapeOptionScale, SceneKit.SCNPhysicsShapeScaleKey
        )
