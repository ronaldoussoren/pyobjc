import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLFeatureDescription (TestCase):
        def testConstants(self):
            self.assertEqual(CoreML.MLModelErrorGeneric, 0)
            self.assertEqual(CoreML.MLModelErrorFeatureType, 1)
            self.assertEqual(CoreML.MLModelErrorIO, 3)
            self.assertEqual(CoreML.MLModelErrorCustomLayer, 4)
            self.assertEqual(CoreML.MLModelErrorCustomModel, 5)

        @min_os_level('10.13')
        @expectedFailureIf(os_level_key(os_release()) < os_level_key('10.14')) # XXX: Documented for 10.13, but doesn't work there???
        def testConstants10_13(self):
            self.assertIsInstance(CoreML.MLModelErrorDomain, unicode)


if __name__ == "__main__":
    main()
