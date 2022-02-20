from PyObjCTools.TestSupport import TestCase
import CoreML


class TestMLMultiArrayShapeConstraintType(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreML.MLMultiArrayShapeConstraintType)

    def test_constants(self):
        self.assertEqual(CoreML.MLMultiArrayShapeConstraintTypeUnspecified, 1)
        self.assertEqual(CoreML.MLMultiArrayShapeConstraintTypeEnumerated, 2)
        self.assertEqual(CoreML.MLMultiArrayShapeConstraintTypeRange, 3)
