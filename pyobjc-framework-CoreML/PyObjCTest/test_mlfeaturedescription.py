import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLFeatureDescription (TestCase):
        @min_os_level("10.13")
        def testMethods10_13(self):
            self.assertResultIsBOOL(CoreML.MLFeatureDescription.isOptional)
            #self.assertArgIsBOOL(CoreML.MLFeatureDescription.setOptional_, 0)
            self.assertResultIsBOOL(CoreML.MLFeatureDescription.isAllowedValue_)

if __name__ == "__main__":
    main()
