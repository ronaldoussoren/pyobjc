from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNRequestHandler (TestCase):
        @min_os_level('10.13')
        def testConstants10_13(self):
            self.assertIsInstance(Vision.VNImageOptionProperties, unicode)
            self.assertIsInstance(Vision.VNImageOptionCameraIntrinsics, unicode)

        @min_os_level('10.13')
        def testMethods10_13(self):
            self.assertResultIsBOOL(Vision.VNImageRequestHandler.performRequests_error_)
            self.assertArgIsOut(Vision.VNImageRequestHandler.performRequests_error_, 1)

            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onCVPixelBuffer_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onCVPixelBuffer_error_, 2)
            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onCVPixelBuffer_orientation_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onCVPixelBuffer_orientation_error_, 3)

            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onCGImage_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onCGImage_error_, 2)
            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onCGImage_orientation_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onCGImage_orientation_error_, 3)

            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onCIImage_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onCIImage_error_, 2)
            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onCIImage_orientation_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onCIImage_orientation_error_, 3)

            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onImageURL_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onImageURL_error_, 2)
            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onImageURL_orientation_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onImageURL_orientation_error_, 3)

            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onImageData_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onImageData_error_, 2)
            self.assertResultIsBOOL(Vision.VNSequenceRequestHandler.performRequests_onImageData_orientation_error_)
            self.assertArgIsOut(Vision.VNSequenceRequestHandler.performRequests_onImageData_orientation_error_, 3)

if __name__ == "__main__":
    main()
