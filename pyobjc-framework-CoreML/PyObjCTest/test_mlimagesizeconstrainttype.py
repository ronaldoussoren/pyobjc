import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLImageSizeConstraintType (TestCase):
        def test_constants(self):
            self.assertEqual(CoreML.MLImageSizeConstraintTypeUnspecified, 0)
            self.assertEqual(CoreML.MLImageSizeConstraintTypeEnumerated, 2)
            self.assertEqual(CoreML.MLImageSizeConstraintTypeRange, 3)


if __name__ == "__main__":
    main()
