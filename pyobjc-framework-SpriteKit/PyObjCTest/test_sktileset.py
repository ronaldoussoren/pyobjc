from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKTileSet(TestCase):
    @min_os_level("10.12")
    def testConstants(self):
        self.assertEqual(SpriteKit.SKTileSetTypeGrid, 0)
        self.assertEqual(SpriteKit.SKTileSetTypeIsometric, 1)
        self.assertEqual(SpriteKit.SKTileSetTypeHexagonalFlat, 2)
        self.assertEqual(SpriteKit.SKTileSetTypeHexagonalPointy, 3)
        self.assertEqual(SpriteKit.SKTileAdjacencyUp, 1 << 0)
        self.assertEqual(SpriteKit.SKTileAdjacencyUpperRight, 1 << 1)
        self.assertEqual(SpriteKit.SKTileAdjacencyRight, 1 << 2)
        self.assertEqual(SpriteKit.SKTileAdjacencyLowerRight, 1 << 3)
        self.assertEqual(SpriteKit.SKTileAdjacencyDown, 1 << 4)
        self.assertEqual(SpriteKit.SKTileAdjacencyLowerLeft, 1 << 5)
        self.assertEqual(SpriteKit.SKTileAdjacencyLeft, 1 << 6)
        self.assertEqual(SpriteKit.SKTileAdjacencyUpperLeft, 1 << 7)
        self.assertEqual(
            SpriteKit.SKTileAdjacencyAll,
            SpriteKit.SKTileAdjacencyUp
            | SpriteKit.SKTileAdjacencyUpperRight
            | SpriteKit.SKTileAdjacencyRight
            | SpriteKit.SKTileAdjacencyLowerRight
            | SpriteKit.SKTileAdjacencyDown
            | SpriteKit.SKTileAdjacencyLowerLeft
            | SpriteKit.SKTileAdjacencyLeft
            | SpriteKit.SKTileAdjacencyUpperLeft,
        )
        self.assertEqual(SpriteKit.SKTileHexFlatAdjacencyUp, 1 << 0)
        self.assertEqual(SpriteKit.SKTileHexFlatAdjacencyUpperRight, 1 << 1)
        self.assertEqual(SpriteKit.SKTileHexFlatAdjacencyLowerRight, 1 << 2)
        self.assertEqual(SpriteKit.SKTileHexFlatAdjacencyDown, 1 << 3)
        self.assertEqual(SpriteKit.SKTileHexFlatAdjacencyLowerLeft, 1 << 4)
        self.assertEqual(SpriteKit.SKTileHexFlatAdjacencyUpperLeft, 1 << 5)
        self.assertEqual(
            SpriteKit.SKTileHexFlatAdjacencyAll,
            SpriteKit.SKTileHexFlatAdjacencyUp
            | SpriteKit.SKTileHexFlatAdjacencyUpperRight
            | SpriteKit.SKTileHexFlatAdjacencyLowerRight
            | SpriteKit.SKTileHexFlatAdjacencyDown
            | SpriteKit.SKTileHexFlatAdjacencyLowerLeft
            | SpriteKit.SKTileHexFlatAdjacencyUpperLeft,
        )
        self.assertEqual(SpriteKit.SKTileHexPointyAdjacencyUpperLeft, 1 << 0)
        self.assertEqual(SpriteKit.SKTileHexPointyAdjacencyUpperRight, 1 << 1)
        self.assertEqual(SpriteKit.SKTileHexPointyAdjacencyRight, 1 << 2)
        self.assertEqual(SpriteKit.SKTileHexPointyAdjacencyLowerRight, 1 << 3)
        self.assertEqual(SpriteKit.SKTileHexPointyAdjacencyLowerLeft, 1 << 4)
        self.assertEqual(SpriteKit.SKTileHexPointyAdjacencyLeft, 1 << 5)
        self.assertEqual(
            SpriteKit.SKTileHexPointyAdjacencyAdd,
            SpriteKit.SKTileHexPointyAdjacencyUpperLeft
            | SpriteKit.SKTileHexPointyAdjacencyUpperRight
            | SpriteKit.SKTileHexPointyAdjacencyRight
            | SpriteKit.SKTileHexPointyAdjacencyLowerRight
            | SpriteKit.SKTileHexPointyAdjacencyLowerLeft
            | SpriteKit.SKTileHexPointyAdjacencyLeft,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyUpEdge,
            SpriteKit.SKTileAdjacencyRight
            | SpriteKit.SKTileAdjacencyLowerRight
            | SpriteKit.SKTileAdjacencyDown
            | SpriteKit.SKTileAdjacencyLowerLeft
            | SpriteKit.SKTileAdjacencyLeft,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyUpperRightEdge,
            SpriteKit.SKTileAdjacencyDown
            | SpriteKit.SKTileAdjacencyLowerLeft
            | SpriteKit.SKTileAdjacencyLeft,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyRightEdge,
            SpriteKit.SKTileAdjacencyDown
            | SpriteKit.SKTileAdjacencyLowerLeft
            | SpriteKit.SKTileAdjacencyLeft
            | SpriteKit.SKTileAdjacencyUpperLeft
            | SpriteKit.SKTileAdjacencyUp,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyLowerRightEdge,
            SpriteKit.SKTileAdjacencyLeft
            | SpriteKit.SKTileAdjacencyUpperLeft
            | SpriteKit.SKTileAdjacencyUp,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyDownEdge,
            SpriteKit.SKTileAdjacencyUp
            | SpriteKit.SKTileAdjacencyUpperRight
            | SpriteKit.SKTileAdjacencyRight
            | SpriteKit.SKTileAdjacencyLeft
            | SpriteKit.SKTileAdjacencyUpperLeft,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyLowerLeftEdge,
            SpriteKit.SKTileAdjacencyUp
            | SpriteKit.SKTileAdjacencyUpperRight
            | SpriteKit.SKTileAdjacencyRight,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyLeftEdge,
            SpriteKit.SKTileAdjacencyUp
            | SpriteKit.SKTileAdjacencyUpperRight
            | SpriteKit.SKTileAdjacencyRight
            | SpriteKit.SKTileAdjacencyLowerRight
            | SpriteKit.SKTileAdjacencyDown,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyUpperLeftEdge,
            SpriteKit.SKTileAdjacencyRight
            | SpriteKit.SKTileAdjacencyLowerRight
            | SpriteKit.SKTileAdjacencyDown,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyUpperRightCorner,
            SpriteKit.SKTileAdjacencyUp
            | SpriteKit.SKTileAdjacencyUpperRight
            | SpriteKit.SKTileAdjacencyRight
            | SpriteKit.SKTileAdjacencyLowerRight
            | SpriteKit.SKTileAdjacencyDown
            | SpriteKit.SKTileAdjacencyLeft
            | SpriteKit.SKTileAdjacencyUpperLeft,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyLowerRightCorner,
            SpriteKit.SKTileAdjacencyUp
            | SpriteKit.SKTileAdjacencyUpperRight
            | SpriteKit.SKTileAdjacencyRight
            | SpriteKit.SKTileAdjacencyLowerRight
            | SpriteKit.SKTileAdjacencyDown
            | SpriteKit.SKTileAdjacencyLowerLeft
            | SpriteKit.SKTileAdjacencyLeft,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyLowerLeftCorner,
            SpriteKit.SKTileAdjacencyUp
            | SpriteKit.SKTileAdjacencyRight
            | SpriteKit.SKTileAdjacencyLowerRight
            | SpriteKit.SKTileAdjacencyDown
            | SpriteKit.SKTileAdjacencyLowerLeft
            | SpriteKit.SKTileAdjacencyLeft
            | SpriteKit.SKTileAdjacencyUpperLeft,
        )
        self.assertEqual(
            SpriteKit.SKTileAdjacencyUpperLeftCorner,
            SpriteKit.SKTileAdjacencyUp
            | SpriteKit.SKTileAdjacencyUpperRight
            | SpriteKit.SKTileAdjacencyRight
            | SpriteKit.SKTileAdjacencyDown
            | SpriteKit.SKTileAdjacencyLowerLeft
            | SpriteKit.SKTileAdjacencyLeft
            | SpriteKit.SKTileAdjacencyUpperLeft,
        )
