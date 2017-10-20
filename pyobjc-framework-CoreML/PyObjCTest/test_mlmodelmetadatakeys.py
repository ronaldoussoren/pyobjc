import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLFeatureDescription (TestCase):
        @min_os_level('10.13')
        def testConstants(self):
            self.assertIsInstance(CoreML.MLModelDescriptionKey, unicode)
            self.assertIsInstance(CoreML.MLModelVersionStringKey, unicode)
            self.assertIsInstance(CoreML.MLModelAuthorKey, unicode)
            self.assertIsInstance(CoreML.MLModelLicenseKey, unicode)
            self.assertIsInstance(CoreML.MLModelCreatorDefinedKey, unicode)


if __name__ == "__main__":
    main()
