import sys

if sys.maxsize > 2 ** 32:
    from PyObjCTools.TestSupport import *
    import CoreML

    class TestMLModel_MLModelCompilation (TestCase):
        @min_os_level("10.13")
        def testMethods10_13(self):
            self.assertArgIsOut(CoreML.MLModel.compileModelAtURL_error_, 1)

if __name__ == "__main__":
    main()
