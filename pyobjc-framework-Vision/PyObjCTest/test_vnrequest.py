from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNRequest (TestCase):
        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertArgIsBlock(Vision.VNRequest.initWithCompletionHandler_, 0, b'v@@')
            self.assertResultIsBOOL(Vision.VNRequest.preferBackgroundProcessing)
            self.assertArgIsBOOL(Vision.VNRequest.setPreferBackgroundProcessing_, 0)
            self.assertResultIsBOOL(Vision.VNRequest.usesCPUOnly)
            self.assertArgIsBOOL(Vision.VNRequest.setUsesCPUOnly_, 0)
            self.assertResultIsBlock(Vision.VNRequest.completionHandler, b'v@@')

        def test_constants(self):
            self.assertEqual(Vision.VNRequestRevisionUnspecified, 0)

if __name__ == "__main__":
    main()
