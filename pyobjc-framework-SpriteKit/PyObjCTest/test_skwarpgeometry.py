from PyObjCTools.TestSupport import TestCase, min_os_level

import SpriteKit


class TestSKWarpGeometry(TestCase):
    @min_os_level("10.12")
    def test_methods10_12(self):
        # Manual bindings because the array size cannot be represented in metadata:
        with self.assertRaisesRegex(TypeError, "expected 4 arguments, got 0"):
            SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_()

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'object'"
        ):
            value = SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
                object(), 10, None, None
            )

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'object'"
        ):
            value = SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
                10, object(), None, None
            )

        value = SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
            5, 10, None, None
        )
        self.assertIsInstance(value, SpriteKit.SKWarpGeometryGrid)

        value = SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
            2, 2, [(n, n) for n in range(9)], None
        )
        self.assertIsInstance(value, SpriteKit.SKWarpGeometryGrid)

        with self.assertRaisesRegex(ValueError, "Expecting value with 2 elements"):
            SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
                2, 2, None, [(n, n, n) for n in range(9)]
            )

        with self.assertRaisesRegex(ValueError, "Expecting value with 2 elements"):
            SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
                2, 2, [(n, n) for n in range(9)], [(n, n, n) for n in range(9)]
            )

        with self.assertRaisesRegex(ValueError, "Expecting value with 2 elements"):
            SpriteKit.SKWarpGeometryGrid.gridWithColumns_rows_sourcePositions_destPositions_(
                2, 2, [(n, n, n) for n in range(9)], None
            )

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

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            value.gridByReplacingSourcePositions_()

        with self.assertRaisesRegex(ValueError, "Expecting value with 2 elements"):
            value.gridByReplacingSourcePositions_([(n, n, n) for n in range(9)])

        newValue = value.gridByReplacingSourcePositions_([(n, n) for n in range(9)])
        self.assertIsInstance(newValue, SpriteKit.SKWarpGeometryGrid)

        with self.assertRaises(TypeError):
            value.gridByReplacingSourcePositions_(None)

        with self.assertRaises(TypeError):
            value.gridByReplacingSourcePositions_([(n, n) for n in range(12)])

        with self.assertRaisesRegex(TypeError, "expected 1 arguments, got 0"):
            value.gridByReplacingDestPositions_()

        with self.assertRaisesRegex(ValueError, "Expecting value with 2 elements"):
            value.gridByReplacingDestPositions_([(n, n, n) for n in range(9)])

        newValue = value.gridByReplacingDestPositions_([(n, n) for n in range(9)])
        self.assertIsInstance(newValue, SpriteKit.SKWarpGeometryGrid)

        with self.assertRaises(TypeError):
            value.gridByReplacingDestPositions_(None)

        with self.assertRaises(TypeError):
            value.gridByReplacingDestPositions_([(n, n) for n in range(12)])
