import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLFeatureType (TestCase):
        def testConstants(self):
            self.assertEqual(CoreML.MLFeatureTypeInvalid, 0)
            self.assertEqual(CoreML.MLFeatureTypeInt64, 1)
            self.assertEqual(CoreML.MLFeatureTypeDouble, 2)
            self.assertEqual(CoreML.MLFeatureTypeString, 3)
            self.assertEqual(CoreML.MLFeatureTypeImage, 4)
            self.assertEqual(CoreML.MLFeatureTypeMultiArray, 5)
            self.assertEqual(CoreML.MLFeatureTypeDictionary, 6)


if __name__ == "__main__":
    main()
