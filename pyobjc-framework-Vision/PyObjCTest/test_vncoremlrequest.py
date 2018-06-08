from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNCoreMLRequest (TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNCoreMLRequestRevision1, 1)

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertArgIsOut(Vision.VNCoreMLModel.modelForMLModel_error_, 1)

            self.assertArgIsBlock(Vision.VNCoreMLRequest.initWithModel_completionHandler_, 1, b'v@@')
            self.assertArgIsBlock(Vision.VNCoreMLRequest.initWithCompletionHandler_, 0, b'v@@')


if __name__ == "__main__":
    main()
