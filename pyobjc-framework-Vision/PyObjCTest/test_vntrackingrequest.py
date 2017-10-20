from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNRequest (TestCase):
        def testConstants(self):
            self.assertEqual(Vision.VNRequestTrackingLevelAccurate, 0)
            self.assertEqual(Vision.VNRequestTrackingLevelFast, 1)

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertResultIsBOOL(Vision.VNTrackingRequest.isLastFrame)
            self.assertArgIsBOOL(Vision.VNTrackingRequest.setLastFrame_, 0)
            self.assertArgIsBlock(Vision.VNTrackingRequest.initWithCompletionHandler_, 0, b'v@@')

if __name__ == "__main__":
    main()
