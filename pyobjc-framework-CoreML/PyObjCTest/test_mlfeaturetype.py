from PyObjCTools.TestSupport import TestCase
import CoreML


class TestMLFeatureType(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreML.MLFeatureType)

    def testConstants(self):
        self.assertEqual(CoreML.MLFeatureTypeInvalid, 0)
        self.assertEqual(CoreML.MLFeatureTypeInt64, 1)
        self.assertEqual(CoreML.MLFeatureTypeDouble, 2)
        self.assertEqual(CoreML.MLFeatureTypeString, 3)
        self.assertEqual(CoreML.MLFeatureTypeImage, 4)
        self.assertEqual(CoreML.MLFeatureTypeMultiArray, 5)
        self.assertEqual(CoreML.MLFeatureTypeDictionary, 6)
