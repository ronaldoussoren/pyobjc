from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLFeatureDescription(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreML.MLModelError)

    def testConstants(self):
        self.assertEqual(CoreML.MLModelErrorGeneric, 0)
        self.assertEqual(CoreML.MLModelErrorFeatureType, 1)
        self.assertEqual(CoreML.MLModelErrorIO, 3)
        self.assertEqual(CoreML.MLModelErrorCustomLayer, 4)
        self.assertEqual(CoreML.MLModelErrorCustomModel, 5)
        self.assertEqual(CoreML.MLModelErrorUpdate, 6)
        self.assertEqual(CoreML.MLModelErrorParameters, 7)
        self.assertEqual(CoreML.MLModelErrorModelDecryptionKeyFetch, 8)
        self.assertEqual(CoreML.MLModelErrorModelDecryption, 9)
        self.assertEqual(CoreML.MLModelErrorModelCollection, 10)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(CoreML.MLModelErrorDomain, str)
