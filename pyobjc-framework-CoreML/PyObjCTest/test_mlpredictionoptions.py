import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLPredictionOptions (TestCase):
        @min_os_level("10.13")
        def testMethods10_13(self):
            self.assertResultIsBOOL(CoreML.MLPredictionOptions.usesCPUOnly)
            self.assertArgIsBOOL(CoreML.MLPredictionOptions.setUsesCPUOnly_, 0)

if __name__ == "__main__":
    main()
