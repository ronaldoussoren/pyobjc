import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLMultiArrayShapeConstraintType (TestCase):
        def test_constants(self):
            self.assertEqual(CoreML.MLMultiArrayShapeConstraintTypeUnspecified, 1)
            self.assertEqual(CoreML.MLMultiArrayShapeConstraintTypeEnumerated, 2)
            self.assertEqual(CoreML.MLMultiArrayShapeConstraintTypeRange, 3)

if __name__ == "__main__":
    main()
