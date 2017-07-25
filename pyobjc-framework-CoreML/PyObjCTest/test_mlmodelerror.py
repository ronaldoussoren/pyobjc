import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLFeatureDescription (TestCase):
        def testConstants(self):
            self.assertEqual(CoreML.MLModelErrorGeneric, 0)
            self.assertEqual(CoreML.MLModelErrorFeatureType, 1)
            self.assertEqual(CoreML.MLModelErrorIO, 3)


if __name__ == "__main__":
    main()
