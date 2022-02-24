from PyObjCTools.TestSupport import TestCase

import GameplayKit


class TestGKMeshGraph(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(GameplayKit.GKMeshGraphTriangulationMode)

    def testConstants(self):
        self.assertEqual(GameplayKit.GKMeshGraphTriangulationModeVertices, 1 << 0)
        self.assertEqual(GameplayKit.GKMeshGraphTriangulationModeCenters, 1 << 1)
        self.assertEqual(GameplayKit.GKMeshGraphTriangulationModeEdgeMidpoints, 1 << 2)
