from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKWarpGeometry(TestCase):
    @min_os_level("10.12")
    def test_methods10_12(self):
        # Manual bindings because the array size cannot be represented in metadata:
        value = SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
            5, 10, None, None
        )
        self.assertIsInstance(value, SpriteKit.SKWarpGeometryGrid)

        value = SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
            2, 2, [(n, n) for n in range(9)], None
        )
        self.assertIsInstance(value, SpriteKit.SKWarpGeometryGrid)

        value = SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
            2, 2, None, [(n, n) for n in range(9)]
        )
        self.assertIsInstance(value, SpriteKit.SKWarpGeometryGrid)

        value = SpriteKit.SKWarpGeometryGrid.alloc().initWithColumns_rows_sourcePositions_destPositions_(
            5, 10, None, None
        )
        self.assertIsInstance(value, SpriteKit.SKWarpGeometryGrid)

        value = SpriteKit.SKWarpGeometryGrid.alloc().initWithColumns_rows_sourcePositions_destPositions_(
            2, 2, [(n, n) for n in range(9)], None
        )
        self.assertIsInstance(value, SpriteKit.SKWarpGeometryGrid)

        value = SpriteKit.SKWarpGeometryGrid.alloc().initWithColumns_rows_sourcePositions_destPositions_(
            2, 2, None, [(n, n) for n in range(9)]
        )
        self.assertIsInstance(value, SpriteKit.SKWarpGeometryGrid)

        newValue = value.gridByReplacingSourcePositions_([(n, n) for n in range(9)])
        self.assertIsInstance(newValue, SpriteKit.SKWarpGeometryGrid)

        with self.assertRaises(TypeError):
            value.gridByReplacingSourcePositions_(None)

        with self.assertRaises(TypeError):
            value.gridByReplacingSourcePositions_([(n, n) for n in range(12)])

        newValue = value.gridByReplacingDestPositions_([(n, n) for n in range(9)])
        self.assertIsInstance(newValue, SpriteKit.SKWarpGeometryGrid)

        with self.assertRaises(TypeError):
            value.gridByReplacingDestPositions_(None)

        with self.assertRaises(TypeError):
            value.gridByReplacingDestPositions_([(n, n) for n in range(12)])
