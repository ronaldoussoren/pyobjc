import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLFeatureDescription(TestCase):
        def testConstants(self):
            self.assertEqual(CoreML.MLModelErrorGeneric, 0)
            self.assertEqual(CoreML.MLModelErrorFeatureType, 1)
            self.assertEqual(CoreML.MLModelErrorIO, 3)
            self.assertEqual(CoreML.MLModelErrorCustomLayer, 4)
            self.assertEqual(CoreML.MLModelErrorCustomModel, 5)
            self.assertEqual(CoreML.MLModelErrorUpdate, 6)
            self.assertEqual(CoreML.MLModelErrorParameters, 7)

        @min_os_level("10.13")
        def testConstants10_13(self):
            self.assertIsInstance(CoreML.MLModelErrorDomain, unicode)


if __name__ == "__main__":
    main()
